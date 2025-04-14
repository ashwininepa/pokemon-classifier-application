# Pokémon Classifier
# FastAPI application for Pokémon image classification
# This FastAPI application provides an endpoint to classify Pokémon images using a pre-trained model.
# The application includes security features such as API key validation and trusted host middleware to enhance security.

# Import libraries and modules
import logging

from fastapi import FastAPI, UploadFile, HTTPException, Request
from app.model import load_model, classify_image
from app.utils.imageFunctions import preprocess_image
from app.api.security import secure_request, generate_api_key
from fastapi.middleware.trustedhost import TrustedHostMiddleware


# Initialize FastAPI app
app = FastAPI()

# Add security middlewares
# Accepts requests from only specified hosts, enhancing security
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["localhost", "127.0.0.1"])

# Generate API key at startup
api_key = generate_api_key() # Generate a secure random API key (64 char hexadecimal string)
logging.basicConfig(level=logging.INFO) # Set up basic logging configuration
logging.info(f"Generated API Key: {api_key}")

# Load the model at startup - ensures that it is ready to use when the first request comes in
logging.info("Loading pre-trained model from HuggingFace...")
model = load_model()

@app.post("/classify/") # Define a POST endpoint at /classify/
@secure_request # A decorator that validates the API key in the incoming request
async def classify_pokemon(request: Request, file: UploadFile):
    """
    Endpoint to classify a Pokémon image.
    """
    if file.content_type not in ["image/jpeg", "image/png"]: # Check if the uploaded file is a JPEG or PNG image - File validation
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a JPEG or PNG image.")

    # Read and preprocess the image
    image_data = await file.read()
    image = preprocess_image(image_data) # convert the image to RGB format and resize it to 224x224 pixels

    # Classify the image
    predictions = classify_image(image, model)
    return {"filename": file.filename, "predictions": predictions}

@app.get("/") # Define a GET endpoint at /
def root():
    """
    Health check endpoint.
    """
    return {"message": "Pokémon Classifier API is running securely!"}