from google.cloud import vision
from tkinter import Tk
from tkinter.filedialog import askopenfilename


# set up the Google Cloud Vision client
client = vision.ImageAnnotatorClient()

# open a file dialog to select an image file
Tk().withdraw()  # hide the root window
image_path = askopenfilename(title="Select an image file", filetypes=[("Image Files", "*.jpeg;*.jpg;*.png")])

if image_path:
    # Load the selected image
    with open(image_path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    
    # Perform label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print("Labels detected in the image:", labels)
    
    # Display the results
    for label in labels:
        print(f"Description: {label.description}, Score: {label.score}")
else:
    print("No file selected.")
    