import cv2
import numpy as np

def adjust_hsv_values():
    """
    Open a window to adjust HSV color range values using trackbars.
    """
    def nothing(x):
        pass

    # Create a window named 'HSV Adjust'
    cv2.namedWindow('HSV Adjust')

    # Create trackbars for lower and upper HSV values
    cv2.createTrackbar('Lower H', 'HSV Adjust', 0, 179, nothing)
    cv2.createTrackbar('Lower S', 'HSV Adjust', 0, 255, nothing)
    cv2.createTrackbar('Lower V', 'HSV Adjust', 0, 255, nothing)
    cv2.createTrackbar('Upper H', 'HSV Adjust', 179, 179, nothing)
    cv2.createTrackbar('Upper S', 'HSV Adjust', 255, 255, nothing)
    cv2.createTrackbar('Upper V', 'HSV Adjust', 255, 255, nothing)

    # Start camera capture (0 is the default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Cannot receive frame.")
            break

        # Get current positions of all trackbars
        lower_h = cv2.getTrackbarPos('Lower H', 'HSV Adjust')
        lower_s = cv2.getTrackbarPos('Lower S', 'HSV Adjust')
        lower_v = cv2.getTrackbarPos('Lower V', 'HSV Adjust')
        upper_h = cv2.getTrackbarPos('Upper H', 'HSV Adjust')
        upper_s = cv2.getTrackbarPos('Upper S', 'HSV Adjust')
        upper_v = cv2.getTrackbarPos('Upper V', 'HSV Adjust')

        # Define lower and upper HSV bounds
        lower_color = np.array([lower_h, lower_s, lower_v])
        upper_color = np.array([upper_h, upper_s, upper_v])

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create mask based on selected color range
        mask = cv2.inRange(hsv, lower_color, upper_color)

        # Bitwise-AND mask and original image
        result = cv2.bitwise_and(frame, frame, mask=mask)

        # Display the original frame and the result
        cv2.imshow('Original', frame)
        cv2.imshow('Masked Result', result)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    adjust_hsv_values()
