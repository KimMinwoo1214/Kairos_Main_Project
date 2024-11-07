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
detected_qr_data = None  # 인식된 QR 코드 데이터 저장

def start_camera():
    global cap, qr_code_detected, detected_qr_data
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
    global qr_code_detected, detected_qr_data
    # QR 코드 인식
    decoded_objects = pyzbar.decode(frame)
    for obj in decoded_objects:
        detected_qr_data = obj.data.decode("utf-8")
        print("QR Code detected:", detected_qr_data)
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
        global qr_code_detected, detected_qr_data
        self.scenario_count += 1  # 시나리오 카운터 증가
        print(f"Starting scenario {self.scenario_count}...")

        # 초기 위치로 이동
        self.move_to_position([0, 0, 0, 0, 0, 0], 5)

        # 첫 번째 위치로 이동
        self.move_to_position([0, -59, -54, 31.7, 90.7, 0], 5)

        # QR 코드 감지 루프
        qr_code_detected = False
        detected_qr_data = None
        print("Searching for QR code...")
        while not qr_code_detected:
            time.sleep(1)  # CPU 사용량을 줄이기 위한 대기

        if qr_code_detected:
            print(f"QR Code '{detected_qr_data}' detected. Executing corresponding action...")

            # QR 코드 데이터에 따른 동작
            if detected_qr_data == "경제":
                self.move_to_position([10, -45, -30, 20, 80, 10], 5)
                self.close_gripper()
            elif detected_qr_data == "소설":
                self.move_to_position([15, -60, -50, 25, 85, 15], 5)
                self.open_gripper()
            elif detected_qr_data == "과학":
                self.move_to_position([-30, -70, -40, 30, 70, -10], 5)
                self.close_gripper()
            elif detected_qr_data == "예술":
                self.move_to_position([20, -50, -45, 15, 75, 5], 5)
                self.open_gripper()
            else:
                print("No predefined action for the detected QR code.")

        # 초기 위치로 복귀
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
