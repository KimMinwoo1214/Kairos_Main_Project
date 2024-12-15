import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Camera calibration matrix and distortion coefficients
mtx = np.array([[310.93505147, 0., 305.1882977],
                [0., 311.02060429, 238.72764315],
                [0., 0., 1.]])  # Camera matrix

dist = np.array([-3.42750945e-01,  1.49543845e-01,  2.39640046e-04,  4.72473300e-04, -3.54611271e-02])  # Distortion coefficients

# Initialize the camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open the camera")
    exit()

print("Press 'q' to exit")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read the frame")
        break

    # Undistort the captured frame
    undistorted_frame = cv2.undistort(frame, mtx, dist)

    # Flip the undistorted frame vertically
    flipped_frame = cv2.flip(undistorted_frame, 0)  # 0: Vertical flip (상/하 반전)

    # Detect QR codes using pyzbar
    decoded_objects = decode(flipped_frame)
    for obj in decoded_objects:
        # Get QR code bounding box coordinates
        x, y, w, h = obj.rect
        # Draw a rectangle around the QR code
        cv2.rectangle(flipped_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Extract and display QR code data
        qr_data = obj.data.decode("utf-8")
        cv2.putText(flipped_frame, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        print(f"Detected QR Code: {qr_data}")

    # Display the flipped frame with the QR codes highlighted
    cv2.imshow("Flipped Undistorted Frame with QR Code", flipped_frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()