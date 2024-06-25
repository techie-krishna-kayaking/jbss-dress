### Flask Color Search Application
This Flask application allows you to search for images containing a specified color. It uses OpenCV for image processing and WebColors for color parsing from user input.

# Getting Started
To run the application locally, follow these steps:

#Clone the repository:
  ```sh
  git clone <repository_url>
  cd <repository_name>
  ```

# Install dependencies:
  Make sure you have Python and pip installed. Then, install the required Python packages:
  ```sh
  pip install flask cv2 numpy webcolors pandas
  ```
  
# Run the application:
  Execute the following command to start the Flask server:
  ```sh
  python app.py
  ```
  
  The application will be accessible at http://localhost:5000 in your web browser.

# Application Structure
  app.py: Main Flask application file containing routes and logic for color searching.
  static/images/: Directory containing sample images for color searching.
  templates/: Directory containing HTML templates for rendering web pages.
  
  # Usage
  Home Page (/): Enter a color in hexadecimal or name format to search for images containing that color.

  Search Results (/search): Displays images from the static/images/ directory that contain the specified color.

# Dependencies
- Flask: Web framework for Python.
- OpenCV: Library for image processing.
- WebColors: Library for parsing color input from users.


# Authors
[Krishna Kayaking] - Creator and developer
