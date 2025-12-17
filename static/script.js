// Init WaveSurfer (Audio Visualizer)
let wavesurfer = WaveSurfer.create({
    container: '#waveform',
    waveColor: '#6366f1',
    progressColor: '#a855f7',
    barWidth: 2,
    height: 60,
    responsive: true,
    cursorColor: 'transparent',
});

const dropZone = document.getElementById('dropZone');
const audioInput = document.getElementById('audioInput');
const fileStatus = document.getElementById('fileStatus');
const processBtn = document.getElementById('processBtn');

// Click to Upload
dropZone.addEventListener('click', () => audioInput.click());

// File Selection Handling
audioInput.addEventListener('change', handleFileSelect);

function handleFileSelect(e) {
    const file = e.target.files[0];
    if (file) {
        validateFile(file);
    }
}

function validateFile(file) {
    // UPDATED: Added MP4 mime types and extension
    const validTypes = [
        'audio/mpeg', 
        'audio/wav', 
        'audio/x-m4a', 
        'audio/mp4', 
        'video/mp4' 
    ];
    
    const extension = file.name.split('.').pop().toLowerCase();
    const validExts = ['mp3', 'wav', 'm4a', 'mp4'];

    if (validTypes.includes(file.type) || validExts.includes(extension)) {
        fileStatus.innerHTML = `<i class="fa-solid fa-file-audio"></i> ${file.name} <br> <span class="valid-file">Ready to Process</span>`;
        processBtn.disabled = false;
        dropZone.style.borderColor = '#4ade80';
    } else {
        fileStatus.innerHTML = `<span style="color:#ef4444">Unsupported file type</span>`;
        processBtn.disabled = true;
    }
}

// Drag and Drop Effects
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});
dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));
dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    if (e.dataTransfer.files.length) {
        audioInput.files = e.dataTransfer.files;
        validateFile(e.dataTransfer.files[0]);
    }
});

// Process Logic
async function processAudio() {
    const file = audioInput.files[0];
    if (!file) return;

    // UI Updates: Disable inputs, show loader
    processBtn.classList.add('hidden');
    document.getElementById('loadingOverlay').classList.remove('hidden');
    document.querySelector('.options-grid').style.opacity = '0.5';
    document.querySelector('.options-grid').style.pointerEvents = 'none';

    // Prepare Data
    const formData = new FormData();
    formData.append('file', file);
    formData.append('denoise', document.getElementById('opt-denoise').checked);
    formData.append('compress', document.getElementById('opt-compress').checked);
    formData.append('eq', document.getElementById('opt-eq').checked);

    try {
        const response = await fetch('/process', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.status === 'success') {
            // Success State
            document.getElementById('loadingOverlay').classList.add('hidden');
            const resultSection = document.getElementById('resultSection');
            resultSection.classList.remove('hidden');

            // Load Visualizer with the new file URL
            wavesurfer.load(data.download_url);
            
            // Auto Download
            const link = document.createElement('a');
            link.href = data.download_url;
            link.download = '';
            document.body.appendChild(link);
            link.click();
            link.remove();
        } else {
            throw new Error(data.error);
        }

    } catch (error) {
        alert("Error: " + error.message);
        location.reload(); // Reset on error
    }
}

// Play/Pause Control
document.getElementById('playPauseBtn').addEventListener('click', () => {
    wavesurfer.playPause();
    const icon = document.querySelector('#playPauseBtn i');
    icon.classList.toggle('fa-play');
    icon.classList.toggle('fa-pause');
});