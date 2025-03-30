from transformers import pipeline


def load_model():
    """
    Load the Pokémon classification model.
    """
    return pipeline("image-classification", model="fufufukakaka/pokemon_image_classifier")