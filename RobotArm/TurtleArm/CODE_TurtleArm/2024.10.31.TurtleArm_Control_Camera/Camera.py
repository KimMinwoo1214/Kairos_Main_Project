import cv2
import serial
import time
import threading

# 아두이노와의 시리얼 포트 설정
port = 'COM6'  # 자신의 포트에 맞게 수정
baudrate = 1000000
ser = serial.Serial(port, baudrate)

time.sleep(2)  # 아두이노와 연결될 때까지 잠시 대기

# 카메라 객체 생성 (기본 카메라는 1번 인덱스, 다른 카메라 사용 시 인덱스 수정)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    ser.close()
    exit()

print("카메라와 시리얼 통신이 시작되었습니다.")

# 각도 입력받기 함수 (별도의 스레드로 실행)
def send_angles():
    while True:
        try:
            angle1 = int(input("첫 번째 서보 각도를 입력하세요 (0-4095): ")) 
            angle2 = int(input("두 번째 서보 각도를 입력하세요 (0-4095): "))
            angle3 = int(input("세 번째 서보 각도를 입력하세요 (0-4095): "))

            # 입력한 각도 값을 아두이노로 전송
            ser.write(f"{angle1},{angle2},{angle3}\n".encode('utf-8'))

        except ValueError:
            print("잘못된 입력입니다. 정수를 입력하세요.")
        except KeyboardInterrupt:
            print("각도 입력을 종료합니다.")
            break

# 각도 입력을 별도의 스레드로 시작
angle_thread = threading.Thread(target=send_angles)
angle_thread.start()

# 카메라 화면 표시
while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    cv2.imshow("Camera", frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
ser.close()
cv2.destroyAllWindows()
