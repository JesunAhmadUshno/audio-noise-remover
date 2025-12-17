# 🎧 SonicClear AI: Studio-Grade Audio Enhancer

![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![Framework](https://img.shields.io/badge/flask-3.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-purple.svg)
![Status](https://img.shields.io/badge/status-stable-success.svg)

> **"Turn amateur recordings into broadcast-quality audio in seconds."**

**SonicClear AI** is a next-generation web application that leverages advanced Digital Signal Processing (DSP) to automatically clean, compress, and master spoken audio. Wrapped in a stunning, modern **Glassmorphism** interface, it brings the power of a professional studio engineer to your browser.

---

## 🚀 Key Features

### 1. 🧠 Intelligent Spectral Gating (Noise Reduction)
Unlike basic filters, SonicClear analyzes the **frequency fingerprint** of your audio.
* **Auto-Profiling**: Captures the first 1 second of audio to establish a "noise profile."
* **FFT Processing**: Uses Fast Fourier Transform to subtract noise frequencies while preserving the human voice.
* **Smart Masking**: Applies a dynamic attenuation mask (0.1 factor) to non-vocal signals.

### 2. 🎚️ Adaptive Dynamic Compression
Achieve that "Radio Voice" consistency.
* **Threshold**: -20dB
* **Ratio**: 4:1
* **Result**: Whispers are lifted, and shouts are tamed, creating a smooth, professional listening experience.

### 3. 🎛️ Broadcast EQ Curve
Automatically applies a "Smiling EQ" curve optimized for speech clarity:
* **Low-End Warmth**: +4dB boost below 250Hz.
* **High-End Air**: +4dB boost above 6kHz for articulation.

### 4. ⚡ Modern Tech Stack
* **Visuals**: Interactive waveform rendering using `wavesurfer.js`.
* **Design**: CSS Glassmorphism with animated background blobs and responsive layout.
* **Backend**: High-performance Python processing with `SciPy` and `Pydub`.

---

## 🛠️ Technology Stack

| Component | Tech | Description |
| :--- | :--- | :--- |
| **Backend Framework** | ![Flask](https://img.shields.io/badge/-Flask-000?style=flat&logo=flask) | Handles API routes and file processing. |
| **DSP Core** | ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat&logo=numpy) | Matrix operations for audio data. |
| **Signal Processing** | ![SciPy](https://img.shields.io/badge/-SciPy-8CAAE6?style=flat&logo=scipy) | STFT, ISTFT, and spectral analysis. |
| **Audio I/O** | **Pydub** | FFmpeg wrapper for format conversion (MP3/WAV/MP4). |
| **Frontend** | **HTML5 / CSS3** | Glassmorphism design system. |
| **Visualization** | **WaveSurfer.js** | WebGL-based audio rendering. |

---

## ⚙️ Installation & Local Setup

Follow these steps to get the studio running on your local machine.

### Prerequisites
1. **Python 3.8+** installed.
2. **FFmpeg** installed (Required for audio processing).
   * *Mac*: `brew install ffmpeg`
   * *Windows*: [Download FFmpeg](https://ffmpeg.org/download.html)
   * *Linux*: `sudo apt install ffmpeg`

### Step 1: Clone the Repository
```bash
git clone [https://github.com/JesunAhmadUshno/audio-noise-remover.git](https://github.com/JesunAhmadUshno/audio-noise-remover.git)
cd audio-noise-remover
Step 2: Install Dependencies
Bash

pip install -r requirements.txt
Step 3: Run the Application
Bash

python app.py
📂 Project Structure
Plaintext

audio-noise-remover/
├── app.py                 # Main Flask Server & Route Logic
├── processor.py           # Core DSP Algorithms (The "Brain")
├── requirements.txt       # Python Dependencies
├── uploads/               # Temporary storage for processing
├── templates/
│   └── index.html         # Main User Interface
└── static/
    ├── style.css          # Glassmorphism Styles & Animations
    └── script.js          # Client-side Logic & Visualizer
🤝 Contributing
Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
Distributed under the MIT License. See LICENSE for more information.

<p align="center"> <b>Built with 💙 by Jesun Ahmad Ushno</b> </p>
