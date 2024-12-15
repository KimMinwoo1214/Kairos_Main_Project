import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Failed to open the camera.")
else:
    # Retrieve the maximum resolution supported by the camera
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # Current width
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # Current height

    print(f"Default Resolution: {int(width)}x{int(height)}")

    # Try setting a high resolution and see what the camera supports
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 9999)  # Arbitrary high value
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 9999)

    # Check the resulting resolution
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(f"Maximum Supported Resolution: {int(width)}x{int(height)}")

cap.release()