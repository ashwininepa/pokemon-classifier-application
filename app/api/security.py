from fastapi import Request, HTTPException
from functools import wraps
import secrets


# Global variable to store the dynamically generated API key
API_KEY = None

def generate_api_key():
    """
    Generate a secure random API key.
    """
    global API_KEY
    API_KEY = secrets.token_hex(32)  # Generate a 64-character hexadecimal key
    return API_KEY

def secure_request(func):
    """
    Decorator to validate the API key in incoming requests.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs): # Retrieves incoming http request
        request: Request = kwargs.get("request")
        if not request:
            raise HTTPException(status_code=500, detail="Request object not found.")

        # Validate the API key from headers
        api_key = request.headers.get("X-API-Key")
        if api_key != API_KEY:
            raise HTTPException(status_code=401, detail="Invalid or missing API key.")
        
        return await func(*args, **kwargs)
    return wrapper