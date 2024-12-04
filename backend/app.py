from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from model.classifier import classify_text
from model.preprocess import extract_text_from_pdf

# Initialize Flask App
app = Flask(__name__)

# Configurations
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route: Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route: File Upload and Classification
@app.route('/classify', methods=['POST'])
def classify_document():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Extract and preprocess text
        if filename.endswith('.pdf'):
            text = extract_text_from_pdf(filepath)
        else:
            with open(filepath, 'r') as f:
                text = f.read()

        if not text.strip():
            return jsonify({'error': 'No text could be extracted from the document'}), 400

        # Perform classification
        labels = ["Mathematics", "Science", "Literature", "Technology"]
        result = classify_text(text, labels)

        # Return results
        return jsonify(result)

    return jsonify({'error': 'Invalid file type'}), 400

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)
