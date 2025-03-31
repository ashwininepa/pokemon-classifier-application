import logging

from fastapi import FastAPI, UploadFile, HTTPException, Request
from app.model import load_model, classify_image
from app.utils.imageFunctions import preprocess_image
from app.api.security import secure_request, generate_api_key
from fastapi.middleware.trustedhost import TrustedHostMiddleware


# Initialize FastAPI app
app = FastAPI()

# Add security middlewares
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["localhost", "0.0.0.0", "127.0.0.1"])

# Generate API key at startup
api_key = generate_api_key()
logging.basicConfig(level=logging.INFO)
logging.info(f"Generated API Key: {api_key}")

# Load the model at startup
model = load_model()

@app.post("/classify/")
@secure_request
async def classify_pokemon(request: Request, file: UploadFile):
    """
    Endpoint to classify a Pokémon image.
    """
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a JPEG or PNG image.")

    # Read and preprocess the image
    image_data = await file.read()
    image = preprocess_image(image_data)

    # Classify the image
    predictions = classify_image(image, model)
    return {"filename": file.filename, "predictions": predictions}

@app.get("/")
def root():
    """
    Health check endpoint.
    """
    return {"message": "Pokémon Classifier API is running securely!"}