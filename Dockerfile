FROM python:3.12-slim

# Set the working directory in the container to /app
WORKDIR /app

COPY . /app

# Install the required packages
RUN pip install --upgrade pip
RUN pip3 install --no-cache -r requirements.txt

# Expose the port the app runs on
EXPOSE 8081

# Command to run the training script
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8081"]