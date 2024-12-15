import cv2
import numpy as np

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

# QR code detector
qr_detector = cv2.QRCodeDetector()

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

    # Detect and decode QR code
    decoded_text, points, _ = qr_detector.detectAndDecode(flipped_frame)
    if points is not None:  # If a QR code is detected
        points = np.int32(points)
        # Draw a polygon around the detected QR code
        for i in range(len(points)):
            pt1 = tuple(points[i][0])
            pt2 = tuple(points[(i + 1) % len(points)][0])
            cv2.line(flipped_frame, pt1, pt2, (0, 255, 0), 2)

        # Display the decoded text on the frame
        if decoded_text:
            cv2.putText(flipped_frame, decoded_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            print(f"Detected QR Code: {decoded_text}")

    # Display the flipped frame with the QR code highlighted
    cv2.imshow("Flipped Undistorted Frame with QR Code", flipped_frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()