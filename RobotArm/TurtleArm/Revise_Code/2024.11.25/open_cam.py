import cv2

cap = cv2.VideoCapture(0)

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
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()