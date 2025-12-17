import numpy as np
import scipy.signal
import scipy.io.wavfile
from pydub import AudioSegment
import os

def process_audio(input_path, output_path, options):
    # 1. Load Audio
    audio = AudioSegment.from_file(input_path)
    sample_rate = audio.frame_rate
    
    # Check options
    do_denoise = options.get('denoise') == 'true'
    do_compress = options.get('compress') == 'true'
    do_eq = options.get('eq') == 'true'

    # Convert to numpy for processing if needed
    if do_denoise or do_eq:
        samples = np.array(audio.get_array_of_samples())
        if audio.channels == 2:
            samples = samples.reshape((-1, 2))
            data = samples[:, 0] # Left channel for analysis
        else:
            data = samples
        
        # Normalize
        data_float = data.astype(np.float32) / np.iinfo(samples.dtype).max

    # --- PROCESS: NOISE REDUCTION ---
    if do_denoise:
        noise_sample_len = min(len(data_float), sample_rate)
        noise_profile = data_float[:noise_sample_len]
        
        f, t, Zxx = scipy.signal.stft(data_float, fs=sample_rate, nperseg=1024)
        _, _, Zxx_noise = scipy.signal.stft(noise_profile, fs=sample_rate, nperseg=1024)
        noise_spectrum = np.mean(np.abs(Zxx_noise), axis=1, keepdims=True)
        
        threshold = 2.0 * noise_spectrum
        mask = np.where(np.abs(Zxx) > threshold, 1.0, 0.1)
        _, denoised_data = scipy.signal.istft(Zxx * mask, fs=sample_rate)
        
        # Reconstruct AudioSegment
        denoised_data_int = (denoised_data * np.iinfo(np.int16).max).astype(np.int16)
        audio = AudioSegment(
            denoised_data_int.tobytes(), 
            frame_rate=sample_rate,
            sample_width=2, 
            channels=1
        )

    # --- PROCESS: COMPRESSION ---
    if do_compress:
        audio = audio.compress_dynamic_range(
            threshold=-20.0, 
            ratio=4.0, 
            attack=5.0, 
            release=50.0
        )

    # --- PROCESS: EQ (Simple Gain) ---
    if do_eq:
        # Pydub simple filter simulation
        # Boost Bass (<250Hz) and Treble (>6kHz)
        audio = audio.low_pass_filter(250).apply_gain(4).overlay(audio)
        # Note: A real parametric EQ is complex in pure Python; this is a simplified "Loudness" effect.

    # Export
    audio.export(output_path, format="mp3")
    return output_path