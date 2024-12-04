from transformers import pipeline

# Load Pre-trained Model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_text(text, labels):
    """
    Classifies the input text into one of the given labels.

    Args:
        text (str): The document text to classify.
        labels (list): List of candidate labels for classification.

    Returns:
        dict: Classification results including the top label and confidence score.
    """
    result = classifier(text[:512], candidate_labels=labels)
    return {
        'category': result['labels'][0],
        'confidence': f"{result['scores'][0] * 100:.2f}%"
    }
