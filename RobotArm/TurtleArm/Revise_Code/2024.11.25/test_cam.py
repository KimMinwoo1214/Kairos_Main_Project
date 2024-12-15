import cv2

# Open the camera
cap = cv2.VideoCapture(0)

# Force MJPG format
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Set resolution (lower values to test compatibility)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Set FPS (adjust if needed)
cap.set(cv2.CAP_PROP_FPS, 30)

if not cap.isOpened():
    print("Failed to open the camera.")
else:
    print("Camera opened successfully!")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame.")
            break

        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    cap.release()
    cv2.destroyAllWindows()
