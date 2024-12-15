import cv2
import numpy as np

# Camera matrix and distortion coefficients from your calibration
mtx = np.array([[317.05966638, 0., 287.9901831 ],
                [0., 317.21510719, 232.81085565],
                [0., 0., 1.]])  # Camera matrix

dist = np.array([-0.3063854, 0.10224856,  0.00108754, -0.00063471, -0.01660539])  # Distortion coefficients

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
