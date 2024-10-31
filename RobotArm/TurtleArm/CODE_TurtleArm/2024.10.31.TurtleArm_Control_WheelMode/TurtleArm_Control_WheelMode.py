import serial
import time

# 아두이노와 통신 설정
arduino = serial.Serial(port='COM6', baudrate=1000000, timeout=1)  # 'COM3'은 포트 이름으로, 환경에 따라 수정 필요
time.sleep(2)  # 아두이노와의 안정적 연결을 위해 잠시 대기

while True:
    try:
        # 사용자로부터 속도 값 입력 받기
        speed = int(input("모터 속도를 입력하세요 (-1000 ~ 1000): "))

        # 속도 값을 아두이노로 전송
        arduino.write(f"{speed}\n".encode())

        # 잠시 대기
        time.sleep(0.5)
    except ValueError:
        print("잘못된 입력입니다. 정수를 입력하세요.")
