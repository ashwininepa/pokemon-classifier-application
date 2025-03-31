from transformers import pipeline


def load_model():
    """
    Load the Pokémon classification model.
    For this task I am using a pre-trained model from Hugging Face.
    The model is taken from the link 'https://huggingface.co/fufufukakaka/pokemon_image_classifier/blob/main/README.md?library=transformers'
    """
    return pipeline("image-classification", model="fufufukakaka/pokemon_image_classifier", use_fast=True)

def classify_image(image, model):
    """
    Classify the given image using the loaded model.
    """
    return model(image)