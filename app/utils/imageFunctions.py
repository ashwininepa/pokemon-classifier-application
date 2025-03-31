from PIL import Image
import io


def preprocess_image(image_data):
    """
    Preprocess the image data for classification.
    """
    image = Image.open(io.BytesIO(image_data)).convert("RGB")
    image = image.resize((224, 224))  # Resize to 224x224
    return image