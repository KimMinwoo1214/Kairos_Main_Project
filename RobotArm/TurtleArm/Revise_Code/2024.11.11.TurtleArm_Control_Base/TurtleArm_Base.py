import serial
import time
import tkinter as tk
from tkinter import ttk

# 아두이노와의 시리얼 포트 설정
port = '/dev/ttyUSB0'  # 자신의 포트에 맞게 수정
baudrate = 1000000
ser = serial.Serial(port, baudrate)

time.sleep(2)  # 아두이노와 연결될 때까지 잠시 대기

# 슬라이더 값 업데이트 함수
def update_servo_angles():
    angle0 = slider0.get()
    angle1 = slider1.get()
    angle2 = slider2.get()
    angle3 = slider3.get()

    # 각도 값을 아두이노로 전송 (,로 구분)
    ser.write(f"{angle0},{angle1},{angle2},{angle3}\n".encode('utf-8'))

    # 각도 값을 레이블에 업데이트
    angle0_label.config(text=f"각도 0: {int(angle0)}")
    angle1_label.config(text=f"각도 1: {int(angle1)}")
    angle2_label.config(text=f"각도 2: {int(angle2)}")
    angle3_label.config(text=f"각도 3: {int(angle3)}")

# Stop 버튼을 눌렀을 때 모든 슬라이더를 2048로 설정하는 함수
def stop_all_servos():
    slider0.set(2048)
    slider1.set(2048)
    slider2.set(2048)
    slider3.set(2048)

    # 각도 값을 아두이노로 전송
    ser.write(f"2048,2048,2048,2048\n".encode('utf-8'))

    # 각도 레이블 업데이트
    angle0_label.config(text=f"각도 0: 2048")
    angle1_label.config(text=f"각도 1: 2048")
    angle2_label.config(text=f"각도 2: 2048")
    angle3_label.config(text=f"각도 3: 2048")

# Tkinter 윈도우 설정
root = tk.Tk()
root.title("서보 모터 각도 조정")

# 0 번째 서보 슬라이더 및 레이블
label0 = ttk.Label(root, text="첫 번째 서보 각도")
label0.pack(pady=10)
slider0 = ttk.Scale(root, from_=0, to_=4095, orient="horizontal", length=300)  # 슬라이더 길이 늘리기
slider0.set(2048)  # 기본값 설정
slider0.pack()
angle0_label = ttk.Label(root, text=f"각도 1: {int(slider0.get())}")
angle0_label.pack()

# 첫 번째 서보 슬라이더 및 레이블
label1 = ttk.Label(root, text="첫 번째 서보 각도")
label1.pack(pady=10)
slider1 = ttk.Scale(root, from_=800, to_=3100, orient="horizontal", length=300)  # 슬라이더 길이 늘리기
slider1.set(2048)  # 기본값 설정
slider1.pack()
angle1_label = ttk.Label(root, text=f"각도 1: {int(slider1.get())}")
angle1_label.pack()

# 두 번째 서보 슬라이더 및 레이블
label2 = ttk.Label(root, text="두 번째 서보 각도")
label2.pack(pady=10)
slider2 = ttk.Scale(root, from_=250, to_=3500, orient="horizontal", length=300)  # 슬라이더 길이 늘리기
slider2.set(2048)  # 기본값 설정
slider2.pack()
angle2_label = ttk.Label(root, text=f"각도 2: {int(slider2.get())}")
angle2_label.pack()

# 세 번째 서보 슬라이더 및 레이블
label3 = ttk.Label(root, text="세 번째 서보 각도")
label3.pack(pady=10)
slider3 = ttk.Scale(root, from_=0, to_=4095, orient="horizontal", length=300)  # 슬라이더 길이 늘리기
slider3.set(2048)  # 기본값 설정
slider3.pack()
angle3_label = ttk.Label(root, text=f"각도 3: {int(slider3.get())}")
angle3_label.pack()

# 슬라이더 값 변경 시마다 레이블 업데이트
slider0.bind("<Motion>", lambda event: angle0_label.config(text=f"각도 0: {int(slider0.get())}"))
slider1.bind("<Motion>", lambda event: angle1_label.config(text=f"각도 1: {int(slider1.get())}"))
slider2.bind("<Motion>", lambda event: angle2_label.config(text=f"각도 2: {int(slider2.get())}"))
slider3.bind("<Motion>", lambda event: angle3_label.config(text=f"각도 3: {int(slider3.get())}"))

# 업데이트 버튼
update_button = ttk.Button(root, text="서보 각도 전송", command=update_servo_angles)
update_button.pack(pady=20)

# Stop 버튼
stop_button = ttk.Button(root, text="Stop (모두 2048로 설정)", command=stop_all_servos)
stop_button.pack(pady=20)

# Tkinter 이벤트 루프 시작
root.mainloop()

# 프로그램 종료 시 아두이노와의 시리얼 연결 종료
ser.close()
