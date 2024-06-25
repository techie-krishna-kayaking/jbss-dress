# Import necessary libraries
from flask import Flask, render_template, request
import os
import cv2
import numpy as np
import webcolors

# Initialize Flask app
app = Flask(__name__)


# Define function to detect color in an image
def detect_color(image_path, target_color):
    # Read the image
    image = cv2.imread(image_path)

    # Convert image to RGB color space
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate mean color of the image
    mean_color = np.mean(rgb_image, axis=(0, 1))

    # Calculate Euclidean distance between mean color and target color
    distance = np.linalg.norm(mean_color - target_color)

    # Set a threshold for color similarity
    threshold = 100

    # Return True if the distance is within the threshold, False otherwise
    return distance < threshold


# Define route for the index page
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Color Search</title>
    </head>
    <body>
        <h1>Color Search</h1>
        <form action="/search" method="post">
            <label for="color">Enter color:</label>
            <input type="text" id="color" name="color">
            <button type="submit">Search</button>
        </form>
    </body>
    </html>
    """


# Define route for the search functionality
@app.route('/search', methods=['POST'])
def search():
    # Get the color input from the form
    color_input = request.form['color']

    # Convert color input to RGB values
    try:
        # Try to parse the color input as a hexadecimal color code
        target_color = webcolors.hex_to_rgb(color_input)
    except ValueError:
        # If parsing fails, try to parse the color input as a color name
        try:
            target_color = webcolors.name_to_rgb(color_input)
        except ValueError:
            # If parsing fails again, return an error message
            return "Invalid color input"

    # Define the directory containing images
    image_dir = 'static/images/'

    # List to store paths of images containing the specified color
    results = []

    # Iterate through each image in the directory
    for filename in os.listdir(image_dir):
        # Check if the file is an image file
        if filename.endswith('.jpg'):
            # Get the full path of the image
            image_path = os.path.join(image_dir, filename)

            # Check if the image contains the specified color
            if detect_color(image_path, target_color):
                # Add the image path to the results list
                results.append(image_path)

    # Generate HTML to display the search results
    result_html = ''
    for result in results:
        result_html += f'<img src="{result}" alt="Image">'

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Search Results</title>
    </head>
    <body>
        <h1>Search Results</h1>
        <div>
            {result_html}
        </div>
    </body>
    </html>
    """


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
