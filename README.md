# 🎧 SonicClear AI: Next-Gen Audio Enhancement

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-3.12-blue.svg) ![Status](https://img.shields.io/badge/status-live-green.svg)

> **"Turn amateur recordings into broadcast-quality audio in seconds."**

SonicClear AI is a state-of-the-art audio processing engine designed to democratize high-fidelity sound. Built with a **Flask** backend and a **Glassmorphism** frontend, it leverages advanced Digital Signal Processing (DSP) algorithms to automatically remove noise, compress dynamic range, and equalize speech.

---

## 🌟 Live Demo
**[Launch SonicClear AI App](https://jesunahmadushno.github.io/audio-noise-remover/)** *(Note: The live demo requires the backend server to be active. See Deployment instructions below.)*

---

## 🚀 Key Features

### 1. 🧠 Intelligent Noise Reduction (Spectral Gating)
Instead of simple filtering, SonicClear analyzes the **spectral footprint** of your audio's background noise (using the first 1 second as a reference profile). It then constructs a dynamic FFT mask to surgically remove noise frequencies while preserving the human voice.

### 2. 🎚️ Adaptive Dynamic Compression
Using a **4:1 ratio** with a **-20dB threshold**, our compressor evens out volume spikes. Whether you're whispering or shouting, the output remains consistent and professional.

### 3. 🎛️ Broadcast EQ Curve
Automatically applies a "Radio Ready" equalization curve:
* **Bass Boost (<250Hz)**: Adds warmth and body to the voice.
* **Treble Sparkle (>6kHz)**: Enhances clarity and articulation.

### 4. ⚡ Instant Waveform Visualization
Powered by `wavesurfer.js`, users get real-time visual feedback of their audio topology before and after processing.

---

## 🛠️ Architecture & Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3 | Glassmorphism UI design with neon accents. |
| **Visualizer** | `wavesurfer.js` | Interactive WebGL-based audio waveform rendering. |
| **Backend** | Python (Flask) | Lightweight REST API to handle file uploads and processing. |
| **DSP Core** | `SciPy` & `NumPy` | Fast Fourier Transforms (FFT) and matrix operations for signal processing. |
| **Audio I/O** | `Pydub` (FFmpeg) | High-speed audio decoding/encoding (supports MP3, WAV, M4A, MP4). |

---

## ⚙️ Local Installation

Get this running on your machine in under 2 minutes.

### Prerequisites
* Python 3.8+
* FFmpeg (Required for audio processing)
    * *Mac*: `brew install ffmpeg`
    * *Windows*: [Download Installer](https://ffmpeg.org/download.html)
    * *Linux*: `sudo apt install ffmpeg`

### 1. Clone & Setup
```bash
git clone [https://github.com/JesunAhmadUshno/audio-noise-remover.git](https://github.com/JesunAhmadUshno/audio-noise-remover.git)
cd audio-noise-remover
