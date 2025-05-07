ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy and install libraries from requirements.txt first to leverage Docker cache
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Install hugging face cli tool
RUN pip install --no-cache-dir huggingface-hub

# Pre-download the model using the transformer-cli
RUN python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='fufufukakaka/pokemon_image_classifier', local_dir='/app/models/pokemon_image_classifier', local_dir_use_symlinks=False)"

# Copy the rest of the application code into the container
COPY . /app

# Expose the port the app runs on
EXPOSE 8081

# Command to run the training script
CMD ["uvicorn", "app.api.main:app", "--host", "127.0.0.1", "--port", "8081"]
