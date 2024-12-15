import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Failed to open the camera.")
else:
    # Check default resolution
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)

    print(f"Default Resolution: {int(width)}x{int(height)}")
    print(f"Default FPS: {fps}")

cap.release()