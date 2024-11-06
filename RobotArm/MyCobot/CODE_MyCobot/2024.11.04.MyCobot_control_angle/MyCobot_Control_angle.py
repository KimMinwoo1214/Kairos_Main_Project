import sys
import threading
import cv2
import time
from pyzbar import pyzbar
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from pymycobot.mycobot import MyCobot

# 전역 변수로 카메라 객체 설정
cap = None
qr_code_detected = False

def start_camera():
    global cap
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # QR 코드 인식
        detect_qr_code(frame)
        cv2.imshow('MyCobot Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def detect_qr_code(frame):
    global qr_code_detected
    # QR 코드 인식
    decoded_objects = pyzbar.decode(frame)
    for obj in decoded_objects:
        print("QR Code detected:", obj.data.decode("utf-8"))
        qr_code_detected = True

class MyCobotController(QWidget):
    def __init__(self):
        super().__init__()
        self.mc = MyCobot('COM7', 115200)
        self.joint_ranges = [(-165, 165), (-165, 165), (-165, 165), (-165, 165), (-165, 165), (-175, 175)]
        self.gripper_state = None
        self.scenario_count = 0  # 시나리오 카운터 초기화
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MyCobot Control')
        self.setGeometry(100, 100, 300, 300)

        vbox = QVBoxLayout()

        # 시나리오 실행 버튼
        scenario_button = QPushButton('Execute Scenario')
        scenario_button.clicked.connect(self.execute_scenario)
        vbox.addWidget(scenario_button)

        self.setLayout(vbox)

    def move_to_position(self, angles, duration):
        for i, angle in enumerate(angles):
            min_angle, max_angle = self.joint_ranges[i]
            if not (min_angle <= angle <= max_angle):
                print(f"Error: Joint {i+1} angle {angle} is out of range ({min_angle} to {max_angle})")
                return

        self.mc.send_angles(angles, 20)
        time.sleep(duration)

    def open_gripper(self):
        self.mc.set_gripper_state(0, 50)
        self.gripper_state = 0
        print("Opening gripper")

    def close_gripper(self):
        self.mc.set_gripper_state(1, 50)
        self.gripper_state = 1
        print("Closing gripper")

    def execute_scenario(self):
        global qr_code_detected
        self.scenario_count += 1  # 시나리오 카운터 증가
        print(f"Starting scenario {self.scenario_count}...")

        # 초기 위치로 이동
        self.move_to_position([0, 0, 0, 0, 0, 0], 5)

        # 첫 번째 위치로 이동
        self.move_to_position([0, -59, -54, 31.7, 90.7, 0], 5)

        # QR 코드 감지 루프
        qr_code_detected = False
        print("Searching for QR code...")
        while not qr_code_detected:
            time.sleep(1)  # CPU 사용량을 줄이기 위한 대기

        if qr_code_detected:
            print("QR Code detected at the first position.")

        # 두 번째 위치로 이동
        self.move_to_position([0, -75.2, -39.6, 33.3, 89, 0], 5)

        # 그리퍼 닫기
        self.close_gripper()
        time.sleep(3)

        # 초기 위치로 복귀
        self.move_to_position([0, 0, 0, 0, 0, 0], 5)

        # 세 번째 위치로 이동
        self.move_to_position([-91.1, -78.1, 0, 0, 0, 0], 5)

        # 그리퍼 열기
        self.open_gripper()
        time.sleep(3)

        # 마지막 종료 위치로 이동
        self.move_to_position([0, 0, 0, 0, 0, 0], 5)

        print("Scenario execution completed.")

if __name__ == '__main__':
    camera_thread = threading.Thread(target=start_camera)
    camera_thread.daemon = True
    camera_thread.start()

    app = QApplication(sys.argv)
    window = MyCobotController()
    window.show()
    sys.exit(app.exec_())
