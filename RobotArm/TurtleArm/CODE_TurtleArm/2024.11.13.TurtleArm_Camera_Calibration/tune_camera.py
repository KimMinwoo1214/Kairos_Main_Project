import cv2
import numpy as np

# Camera matrix and distortion coefficients from your calibration
mtx = np.array([[310.93505147, 0., 305.1882977 ],
                [0., 311.02060429, 238.72764315],
                [0., 0., 1.]])  # Camera matrix

dist = np.array([-3.42750945e-01,  1.49543845e-01,  2.39640046e-04,  4.72473300e-04, -3.54611271e-02])  # Distortion coefficients

# Open the webcam (camera 0, usually the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# Get the camera frame width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a window to show the live video stream
cv2.namedWindow("Live Video", cv2.WINDOW_NORMAL)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture frame")
        break

    # Undistort the captured frame using the camera matrix and distortion coefficients
    undistorted_frame = cv2.undistort(frame, mtx, dist)

    # Display the original and undistorted frames side by side (optional)
    cv2.imshow("Live Video - Undistorted", undistorted_frame)

    # Press 'q' to quit the live video feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
