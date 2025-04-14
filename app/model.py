import logging
from transformers import pipeline

from app.utils.globals import LABEL_TRANSLATIONS


def load_model():
    """
    Load the Pokémon classification model.
    For this task I am using a pre-trained model from Hugging Face.
    The model is taken from the link 'https://huggingface.co/fufufukakaka/pokemon_image_classifier/blob/main/README.md?library=transformers'
    """
    logging.info("Loading pre-trained model from HuggingFace...")
    try:
        model = pipeline("image-classification", model="/app/models/pokemon_image_classifier", use_fast=True)
        logging.info("Model loaded successfully.")
        return model
    except Exception as e:
        logging.error(f"Error loading model: {e}")
        raise RuntimeError("Failed to load model. Please check the model path and try again.")

def classify_image(image, model):
    """
    Classify the given image using the loaded model.
    """
    predictions = model(image)
    top_prediction = max(predictions, key=lambda x: x["score"])
    # Convert the score to percentage
    top_prediction['score'] = round(top_prediction['score'] * 100, 2)
    # Translate the label if it exists in the dictionary
    top_prediction['label'] = LABEL_TRANSLATIONS.get(top_prediction['label'], top_prediction['label'])
    
    return predictions