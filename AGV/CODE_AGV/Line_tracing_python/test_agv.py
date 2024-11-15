import time
from pymycobot.myagv import MyAgv

# MyAGV 객체 생성 (포트를 상황에 맞게 수정)
myagv = MyAgv('/dev/ttyAMA2', 115200)
time.sleep(2)  # AGV 초기화 대기

def test_led():
    print("Setting LED to red.")
    myagv.set_led(1, 255, 0, 0)  # 빨간색 LED 켜기
    time.sleep(1)
    
    print("Setting LED to green.")
    myagv.set_led(1, 0, 255, 0)  # 녹색 LED 켜기
    time.sleep(1)
    
    print("Setting LED to blue.")
    myagv.set_led(1, 0, 0, 255)  # 파란색 LED 켜기
    time.sleep(1)
    
    print("Setting LED to blink.")
    myagv.set_led(2, 255, 255, 255)  # LED를 깜박이게 설정
    time.sleep(2)

    myagv.set_led(1, 91, 10, 145)
    time.sleep(1)

def test_movement():
    print("Moving forward.")
    myagv.go_ahead(10, 1)  # 앞으로 이동
    time.sleep(0.1)
    
    print("Moving backward.")
    myagv.retreat(10, 1)  # 뒤로 이동
    time.sleep(0.1)
    
    print("Panning left.")
    myagv.pan_left(5, 1)  # 왼쪽으로 이동
    time.sleep(0.1)
    
    print("Panning right.")
    myagv.pan_right(5, 1)  # 오른쪽으로 이동
    time.sleep(0.1)
    
    print("Rotating clockwise.")
    myagv.clockwise_rotation(15, 1)  # 시계 방향 회전
    time.sleep(0.1)
    
    print("Rotating counterclockwise.")
    myagv.counterclockwise_rotation(15, 1)  # 반시계 방향 회전
    time.sleep(0.1)
    
    print("Stopping AGV.")
    myagv.stop()  # 정지

def test_battery_info():
    print("Getting battery information.")
    battery_info = myagv.get_battery_info()
    print(f"Battery info: {battery_info}")

def test_firmware_version():
    print("Getting firmware version.")
    firmware_version = myagv.get_firmware_version()
    print(f"Firmware version: {firmware_version}")

def test_motor_current():
    print("Getting motor current.")
    motor_current = myagv.get_motors_current()
    print(f"Motor current: {motor_current}")

def main():
    print("Starting AGV API tests.")
    test_led()
    test_movement()
    test_battery_info()
    test_firmware_version()
    test_motor_current()
    print("AGV API tests completed.")

if __name__ == "__main__":
    main()
