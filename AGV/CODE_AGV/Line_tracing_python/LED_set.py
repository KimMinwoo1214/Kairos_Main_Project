import time
from pymycobot.myagv import MyAgv

# MyAGV 객체 생성 (포트를 상황에 맞게 수정)
myagv = MyAgv('/dev/ttyAMA2', 115200)
time.sleep(2)  # AGV 초기화 
print("Setting LED to red.")
myagv.set_led(1, 91, 10, 145)  # 빨간색 LED 켜기
