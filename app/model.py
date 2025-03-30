from transformers import pipeline


def load_model():
    """
    Load the Pokémon classification model.
    """
    return pipeline("image-classification", model="fufufukakaka/pokemon_image_classifier")

def classify_image(image, model):
    """
    Classify the given image using the loaded model.
    """
    return model(image)