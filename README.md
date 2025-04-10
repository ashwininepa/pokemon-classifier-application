# Pokemon Classifier Application

This is a containerized application that uses a pre-trained model from Hugging Face to classify Pokemon images.

## Features
- Exposes a REST API to classify Pokémon images.
- Dynamically loads the pre-trained model using Hugging Face's `pipeline()`.
- Dynamically generates an API key at startup.
- Includes security features like API key validation.

## Security Features
1. **API Key Authentication**: All endpoints require a valid API key in the `X-API-Key` header.
1. **File Validation**: Ensures only valid image files (JPEG/PNG) are accepted.

## How to Run
1. Build the Docker image:
   ```bash
   docker build -t pokemon-classifier-api .
2. docker run -it -p 8081:8081 pokemon-classifier-api uvicorn app.api.main:app --host 0.0.0.0 --port 8081 --reload

docker run 
> creates and start a new container from a specified docker image
-it 
   > i (interactive) keeps the containers standard input open and allows us to interact with the container
    > t (try) allocates a psuedo-TTY (terminal) for the container, making it easier to interact with the container terminal
> together, it is good for debugging or running containers interactively
> -p 8081:8081 > maps a port from the container to the host machine (first one is accessible on host machine and second one is the container port)
Allows to access the app running inside the container from host machine at http://localhost:8081
> name_of_app/image that tells docker which image to use to create a container
> uvicron .... --reload 
   > uvicorn is a lightweight ASGI server used to run FastAPI applications
   > app.api.main.app: path to python module where FastAPI is defined (path_to_main.py)
   > --host: binds the application to all available network interfaces inside the container, making it accessible from outside the container
   > port: specifies the port on which the app will run inside the container
   > --reload: enables live reloading that automatically restarts the server when code changes are detected

3. Test the API: Use Postman
4. Check the response for the classification result.

Some useful docker commands:
docker logs image_name/container_id
docker ps
docker info

# Resources
1. The model used in this task is from HuggingFace and can be found at 'https://huggingface.co/fufufukakaka/pokemon_image_classifier/blob/main/README.md?library=transformers'
1. The dataset is used from an archieved repo and can be found at 'https://github.com/kjaisingh/Pokemon-Classifier/tree/master/dataset'
1. I have also taken help from Copilot where needed and have referred to some of my previous works to sharpen my code a bit as its always good to go back in time a bit.

