import serial
import time
import tkinter as tk
from tkinter import ttk
import cv2  # OpenCV 사용
from pyzbar.pyzbar import decode  # pyzbar 라이브러리 사용

# 아두이노와의 시리얼 포트 설정
port = 'COM9'  # 자신의 포트에 맞게 수정
baudrate = 1000000
ser = serial.Serial(port, baudrate)
time.sleep(2)  # 아두이노 연결 대기

# 작업 위치에 따른 각도 값 설정
QR_SCAN_ANGLE = [3072, 2014, 2660, 2048]  # QR 코드 스캔 위치
PICKUP_ANGLE = [3072, 1440, 2100, 2048]   # 책 집는 위치
STORE1_ANGLE = [4095, 2300, 2625, 2048]    # 책 수납1 위치
STORE2_ANGLE = [4095, 2000, 3330, 2048]    # 책 수납2 위치
STOP_ANGLE = [2048, 2048, 2048, 2048]    # 윈위치

# 특정 위치로 이동하는 함수
def move_to_position(angles):
    ser.write(f"{angles[0]},{angles[1]},{angles[2]},{angles[3]}\n".encode('utf-8'))
    print(f"Moving to position: {angles}")
    time.sleep(1)

# QR 코드 인식 함수
def scan_qr_code():
    cap = cv2.VideoCapture(0)  # 기본 카메라 사용

    print("QR 코드 인식을 시작합니다...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("카메라에서 프레임을 가져올 수 없습니다.")
            break

        # QR 코드 인식
        qr_codes = decode(frame)
        for qr_code in qr_codes:
            qr_data = qr_code.data.decode('utf-8')
            print(f"QR 코드 인식됨: {qr_data}")
            cap.release()
            cv2.destroyAllWindows()
            return qr_data  # 인식된 QR 코드 데이터 반환

        # 화면에 영상 출력
        cv2.imshow("QR 코드 스캔", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
   
# QR 스캔 위치로 이동 후 QR 코드 인식
def move_to_qr_scan():
    move_to_position(QR_SCAN_ANGLE)
    print("QR 코드 스캔 위치로 이동")
    scan_qr_code()  # QR 코드 스캔 함수 호출

# 책 집는 위치로 이동
def move_to_pickup():
    move_to_position(PICKUP_ANGLE)
    print("책 집는 위치로 이동")

# 책 수납 위치로 이동
def move_to_store1():
    move_to_position(STORE1_ANGLE)
    print("책 수납 위치1로 이동")

# 책 수납 위치로 이동
def move_to_store2():
    move_to_position(STORE2_ANGLE)
    print("책 수납 위치1로 이동")

def stop():
    move_to_position(STOP_ANGLE)
    print("원위치 정렬")

# 그리퍼 제어 함수
def send_gripper_command(action):
    command = f"GRIPPER:{action}\n"
    ser.write(command.encode())
    print(f"Sent to TurtleArm: {command.strip()}")

# GUI 설정
root = tk.Tk()
root.title("TurtleArm 제어")

# 버튼 설정
qr_button = ttk.Button(root, text="QR 스캔 위치로 이동", command=move_to_qr_scan)
qr_button.pack(pady=10)

pickup_button = ttk.Button(root, text="책 집는 위치로 이동", command=move_to_pickup)
pickup_button.pack(pady=10)

store1_button = ttk.Button(root, text="책 수납 위치로 이동", command=move_to_store1)
store1_button.pack(pady=10)

store2_button = ttk.Button(root, text="책 수납 위치로 이동", command=move_to_store2)
store2_button.pack(pady=10)

# 그리퍼 제어 버튼 설정
grip_button = ttk.Button(root, text="그리퍼 잡기", command=lambda: send_gripper_command("GRIP"))
grip_button.pack(pady=10)

release_button = ttk.Button(root, text="그리퍼 놓기", command=lambda: send_gripper_command("RELEASE"))
release_button.pack(pady=10)

stop_button = ttk.Button(root, text="원위치", command=stop)
stop_button.pack(pady=10)

root.mainloop()
ser.close()
