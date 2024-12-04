import PyPDF2

def extract_text_from_pdf(filepath):
    """
    Extracts text from a PDF file.

    Args:
        filepath (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    try:
        with open(filepath, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''.join([page.extract_text() for page in reader.pages])
        return text
    except Exception as e:
        return f"Error extracting text: {str(e)}"

def preprocess_text(text):
    """
    Cleans and preprocesses the text.

    Args:
        text (str): The raw text to preprocess.

    Returns:
        str: Cleaned and preprocessed text.
    """
    # Example: Convert to lowercase, remove unnecessary spaces
    return text.lower().strip()
