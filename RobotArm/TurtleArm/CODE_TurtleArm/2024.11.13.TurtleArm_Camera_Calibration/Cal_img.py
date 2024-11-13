import cv2
import os
from datetime import datetime

# Specify the directory where you want to save the images
save_directory = '/home/pi/Revise_Code/2024.11.13.TurtleArm_Camera_Calibration'  # Change this path as needed

# Create the directory if it does not exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Initialize the camera (0 is the default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the camera")
    exit()

# Initialize a counter for the image number
image_counter = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image")
        break

    # Display the resulting frame
    cv2.imshow('Camera Feed', frame)

    # Wait for key press (wait for 's' to save image, 'q' to quit)
    key = cv2.waitKey(1) & 0xFF

    # Save image when 's' is pressed
    if key == ord('s'):
        # Create a filename using the image_counter
        image_filename = f'{save_directory}/captured_image_{image_counter}.jpg'
        cv2.imwrite(image_filename, frame)
        print(f"Image saved as '{image_filename}'")

        # Increment the counter for the next image
        image_counter += 1

    # Exit the loop when 'q' is pressed
    elif key == ord('q'):
        print("Exiting...")
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
