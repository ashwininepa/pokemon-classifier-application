from PIL import Image
import io


def preprocess_image(image_data):
    """
    Preprocess the image data for classification.
    """
    image = Image.open(io.BytesIO(image_data)).convert("RGB")
    return image