const form = document.getElementById('upload-form');
const resultDiv = document.getElementById('result');
const categorySpan = document.getElementById('category');
const confidenceSpan = document.getElementById('confidence');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById('file');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please upload a file!');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('/classify', {
        method: 'POST',
        body: formData,
    });

    if (response.ok) {
        const data = await response.json();
        categorySpan.textContent = data.category;
        confidenceSpan.textContent = data.confidence;
        resultDiv.classList.remove('hidden');
    } else {
        alert('Error: Unable to classify the document.');
    }
});
