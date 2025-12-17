from flask import Flask, request, send_file, render_template, jsonify, url_for
import os
from processor import process_audio

# REMOVED: template_folder='static'
app = Flask(__name__) 

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    options = {
        'denoise': request.form.get('denoise'),
        'compress': request.form.get('compress'),
        'eq': request.form.get('eq')
    }

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    output_filename = f"processed_{file.filename.rsplit('.', 1)[0]}.mp3"
    output_path = os.path.join(UPLOAD_FOLDER, output_filename)
    
    file.save(filepath)
    
    try:
        process_audio(filepath, output_path, options)
        # Note: We use a relative path for the download URL
        return jsonify({'status': 'success', 'download_url': f'/download/{output_filename}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)