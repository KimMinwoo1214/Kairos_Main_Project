import sys
import threading
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from pymycobot.mycobot import MyCobot
import time

# 전역 변수로 카메라 객체 설정
cap = None
i = 0  # 이미지 인덱스 변수

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

        cv2.imshow('MyCobot Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

class MyCobotController(QWidget):
    def __init__(self):
        super().__init__()
        self.mc = MyCobot('COM7', 115200)
        self.joint_ranges = [
            (-1600, 1600),  # 조인트 범위를 0.1 단위로 확장
            (-850, 900),
            (-1800, 450),
            (-1600, 1600),
            (-1000, 1000),
            (-1800, 1800),
        ]
        self.mc.set_gripper_state(0,20)
        self.joint_angles = [0, 0, 0, 0, 0, 0]
        self.gripper_state = None
        self.saved_states = []
        self.filepath_input = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MyCobot Real-time Angle and Coordinates Display with Gripper Control')
        self.setGeometry(100, 100, 400, 700)

        vbox = QVBoxLayout()
        self.sliders = []
        self.labels = []

        for i in range(6):
            hbox = QHBoxLayout()
            label = QLabel(f'Joint {i+1} Angle: {self.joint_angles[i]:.1f}')
            self.labels.append(label)
            hbox.addWidget(label)

            slider = QSlider(Qt.Horizontal)
            slider.setMinimum(self.joint_ranges[i][0])
            slider.setMaximum(self.joint_ranges[i][1])
            slider.setValue(0)
            slider.valueChanged.connect(lambda value, i=i: self.update_joint_angle(i, value))
            self.sliders.append(slider)
            hbox.addWidget(slider)

            vbox.addLayout(hbox)

        self.coords_label = QLabel('Coordinates (x, y, z, rx, ry, rz): (0, 0, 0, 0, 0, 0)')
        vbox.addWidget(self.coords_label)

        gripper_hbox = QHBoxLayout()
        self.gripper_open_button = QPushButton('Close Gripper')
        self.gripper_open_button.clicked.connect(self.open_gripper)
        gripper_hbox.addWidget(self.gripper_open_button)

        self.gripper_close_button = QPushButton('Open Gripper')
        self.gripper_close_button.clicked.connect(self.close_gripper)
        gripper_hbox.addWidget(self.gripper_close_button)

        vbox.addLayout(gripper_hbox)

        # "(0, 0, 0, 0, 0, 0)"으로 이동하는 버튼 추가
        move_home_button = QPushButton('Move to (0, 0, 0, 0, 0, 0)')
        move_home_button.clicked.connect(self.move_to_home)
        vbox.addWidget(move_home_button)

        save_position_button = QPushButton('Save Current Position')
        save_position_button.clicked.connect(self.save_current_position)
        vbox.addWidget(save_position_button)

        self.filepath_input = QLineEdit(self)
        self.filepath_input.setPlaceholderText('Enter file path to save images (e.g., /home/user/images)')
        vbox.addWidget(self.filepath_input)

        save_image_button = QPushButton('Save Image')
        save_image_button.clicked.connect(self.save_image)
        vbox.addWidget(save_image_button)

        self.repeat_input = QLineEdit()
        self.repeat_input.setPlaceholderText('Enter repeat count')
        vbox.addWidget(self.repeat_input)

        repeat_button = QPushButton('Repeat Saved Movements')
        repeat_button.clicked.connect(self.repeat_saved_movements)
        vbox.addWidget(repeat_button)

        stop_button = QPushButton('Stop')
        stop_button.clicked.connect(self.stop_movement)
        vbox.addWidget(stop_button)

        self.setLayout(vbox)

    def update_joint_angle(self, joint_index, value):
        # 슬라이더 값을 소수점 첫째 자리로 변환
        angle = value / 10.0
        self.joint_angles[joint_index] = angle
        self.labels[joint_index].setText(f'Joint {joint_index+1} Angle: {angle:.1f}')
        self.mc.send_angle(joint_index + 1, angle, 20)
        self.update_coordinates()

    def move_to_home(self):
        # 모든 조인트를 0도로 이동
        for i in range(6):
            self.mc.send_angle(i + 1, 0, 20)
            self.sliders[i].setValue(0)
            self.labels[i].setText(f'Joint {i+1} Angle: 0')
        self.coords_label.setText('Coordinates (x, y, z, rx, ry, rz): (0, 0, 0, 0, 0, 0)')

    def update_coordinates(self):
        coords = self.mc.get_coords()
        if coords:
            self.coords_label.setText(f'Coordinates (x, y, z, rx, ry, rz): {tuple(coords)}')

    def stop_movement(self):
        for i in range(6):
            self.mc.send_angle(i + 1, 0, 20)
            self.sliders[i].setValue(0)
            self.labels[i].setText(f'Joint {i+1} Angle: 0')
        self.coords_label.setText('Coordinates (x, y, z, rx, ry, rz): (0, 0, 0, 0, 0, 0)')

    def open_gripper(self):
        self.mc.set_gripper_state(1, 50)
        self.gripper_state = 1
        print("Gripper Closed.")

    def close_gripper(self):
        self.mc.set_gripper_state(0, 50)
        self.gripper_state = 0
        print("Gripper Opened.")

    def save_image(self):
        global cap, i
        filepath = self.filepath_input.text().strip()
        if cap is not None and filepath:
            ret, frame = cap.read()
            if ret:
                filename = f"{filepath}/Red_{i}.png"
                cv2.imwrite(filename, frame)
                print(f"Image saved as {filename}")
                i += 1
            else:
                print("Failed to capture image")
        else:
            print("Camera not initialized or file path not set")

    def save_current_position(self):
        state = {'angles': self.joint_angles.copy(), 'gripper': self.gripper_state}
        self.saved_states.append(state)
        print(f"Position saved: {state}")

    def repeat_saved_movements(self):
        try:
            repeat_count = int(self.repeat_input.text())
        except ValueError:
            print("Invalid repeat count")
            return

        for _ in range(repeat_count):
            for state in self.saved_states:
                for i, angle in enumerate(state['angles']):
                    self.mc.send_angle(i + 1, angle, 20)
                    time.sleep(0.5)
                if state['gripper'] == 1:
                    self.mc.set_gripper_state(1, 50)
                else:
                    self.mc.set_gripper_state(0, 50)
                time.sleep(1)
            print(f"One cycle completed")
        print(f"Repeated {repeat_count} times")

if __name__ == '__main__':
    camera_thread = threading.Thread(target=start_camera)
    camera_thread.daemon = True
    camera_thread.start()

    app = QApplication(sys.argv)
    window = MyCobotController()
    window.show()
    sys.exit(app.exec_())
