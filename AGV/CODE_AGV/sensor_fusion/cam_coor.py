import cv2

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(f"Mouse Position: x={x}, y={y}")

def main():
    # 카메라 장치 열기
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # OpenCV 창 열기
    cv2.namedWindow("Camera Image")
    cv2.setMouseCallback("Camera Image", mouse_callback)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # 이미지 보여주기
        cv2.imshow("Camera Image", frame)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 자원 해제
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

