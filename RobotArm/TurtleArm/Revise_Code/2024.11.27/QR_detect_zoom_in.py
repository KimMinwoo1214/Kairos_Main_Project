import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Camera calibration matrix and distortion coefficients
mtx = np.array([[317.05966638, 0., 287.9901831 ],
                [0., 317.21510719, 232.81085565],
                [0., 0., 1.]])  # Camera matrix

dist = np.array([-0.3063854, 0.10224856,  0.00108754, -0.00063471, -0.01660539])  # Distortion coefficients

# Initialize the camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open the camera")
    exit()

print("Press 'q' to exit")

zoom_factor = 2  # Initial ZOOM-IN factor (1.5x)
zoom_mode = True  # Enable ZOOM-IN mode from the start
zoom_x1, zoom_y1, zoom_x2, zoom_y2 = 0, 0, 0, 0  # 초기 ROI

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

    # Initial ZOOM-IN logic
    if zoom_mode and zoom_x1 == 0 and zoom_x2 == 0:  # 첫 번째 프레임에서 ROI를 설정
        h, w = flipped_frame.shape[:2]
        center_x, center_y = w // 2, h // 2  # Frame center
        half_w, half_h = int(w // (2 * zoom_factor)), int(h // (2 * zoom_factor))

        # Calculate initial zoomed ROI
        zoom_x1 = max(center_x - half_w, 0)
        zoom_y1 = max(center_y - half_h, 0)
        zoom_x2 = min(center_x + half_w, w)
        zoom_y2 = min(center_y + half_h, h)

    # Apply ZOOM-IN if zoom_mode is enabled
    if zoom_mode:
        zoomed_frame = flipped_frame[int(zoom_y1):int(zoom_y2), int(zoom_x1):int(zoom_x2)]
        if zoomed_frame.size > 0:
            flipped_frame = cv2.resize(zoomed_frame, (flipped_frame.shape[1], flipped_frame.shape[0]), interpolation=cv2.INTER_LINEAR)

    # Detect QR codes using pyzbar
    decoded_objects = decode(flipped_frame)
    for obj in decoded_objects:
        x, y, w, h = obj.rect
        # Draw a rectangle around the QR code
        cv2.rectangle(flipped_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display QR code data
        qr_data = obj.data.decode("utf-8")
        cv2.putText(flipped_frame, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        print(f"Detected QR Code: {qr_data}")

    # Display the flipped frame
    cv2.imshow("Flipped Undistorted Frame with QR Code", flipped_frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
