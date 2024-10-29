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
    cap = cv2.VideoCapture(0)  # 카메라 시작

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow('TurtleArm Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

class MyCobotController(QWidget):
    def __init__(self):
        super().__init__()

        # MyCobot 연결 설정
        self.mc = MyCobot('COM6', 115200)

        # 각 조인트의 각도 범위 설정
        self.joint_ranges = [
            (0, 4095),  # 1번 조인트
            (0, 4095),    # 2번 조인트
            (0, 4095),   # 3번 조인트
            (0, 4095),  # 4번 조인트
            # (0, 4095),  # 5번 조인트
            # (0, 4095),  # 6번 조인트
        ]
        
        self.joint_angles = [0, 0, 0, 0, 0, 0]  # 초기 각도 설정
        self.saved_states = []  # 저장된 각도 상태
        
        # 경로 입력 필드
        self.filepath_input = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TurtleArm Real-time Angle and Coordinates Display')
        self.setGeometry(100, 100, 400, 700)

        # 레이아웃 생성
        vbox = QVBoxLayout()

        # 각 슬라이더와 라벨 추가
        self.sliders = []
        self.labels = []
        for i in range(6):
            hbox = QHBoxLayout()
            
            label = QLabel(f'Joint {i+1} Angle: {self.joint_angles[i]}')
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

        # 좌표값을 표시할 라벨 추가
        self.coords_label = QLabel('Coordinates (x, y, z, rx, ry, rz): (0, 0, 0, 0, 0, 0)')
        vbox.addWidget(self.coords_label)

        # 위치 저장
        save_position_button = QPushButton('Save Current Position')
        save_position_button.clicked.connect(self.save_current_position)
        vbox.addWidget(save_position_button)
        
        # 경로 입력 필드 추가
        self.filepath_input = QLineEdit(self)
        self.filepath_input.setPlaceholderText('Enter file path to save images (e.g., /home/user/images)')
        vbox.addWidget(self.filepath_input)

        # 이미지 저장 버튼 추가
        save_image_button = QPushButton('Save Image')
        save_image_button.clicked.connect(self.save_image)
        vbox.addWidget(save_image_button)

        # 반복 입력 필드 및 버튼 추가
        self.repeat_input = QLineEdit()
        self.repeat_input.setPlaceholderText('Enter repeat count')
        vbox.addWidget(self.repeat_input)

        repeat_button = QPushButton('Repeat Saved Movements')
        repeat_button.clicked.connect(self.repeat_saved_movements)
        vbox.addWidget(repeat_button)

        # 정지 버튼 추가
        stop_button = QPushButton('Stop')
        stop_button.clicked.connect(self.stop_movement)
        vbox.addWidget(stop_button)

        self.setLayout(vbox)

    def update_joint_angle(self, joint_index, value):
        # 슬라이더 값에 따라 각도 업데이트
        self.joint_angles[joint_index] = value
        self.labels[joint_index].setText(f'Joint {joint_index+1} Angle: {value}')
        
        # 각도를 0 ~ 4095 범위로 변환하여 전송
        mapped_angle = int(((value - self.joint_ranges[joint_index][0]) / 
                            (self.joint_ranges[joint_index][1] - self.joint_ranges[joint_index][0])) * 4095)
        self.mc.send_angle(joint_index + 1, mapped_angle, 20)

        # 각도 변경 후 좌표 업데이트
        self.update_coordinates()

    def update_coordinates(self):
        # 로봇의 현재 좌표를 가져와서 표시
        coords = self.mc.get_coords()  # (x, y, z, rx, ry, rz)
        if coords:
            self.coords_label.setText(f'Coordinates (x, y, z, rx, ry, rz): {tuple(coords)}')

    def stop_movement(self):
        # 모든 관절을 0도로 리셋
        for i in range(6):
            self.mc.send_angle(i + 1, 0, 20)
            self.sliders[i].setValue(0)
            self.labels[i].setText(f'Joint {i+1} Angle: 0')
        
        self.coords_label.setText('Coordinates (x, y, z, rx, ry, rz): (0, 0, 0, 0, 0, 0)')

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
        # 현재 각도를 저장
        state = {
            'angles': self.joint_angles.copy()
        }
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
                # 각 관절 각도 복원
                for i, angle in enumerate(state['angles']):
                    mapped_angle = int(((angle - self.joint_ranges[i][0]) / 
                                        (self.joint_ranges[i][1] - self.joint_ranges[i][0])) * 4095)
                    self.mc.send_angle(i + 1, mapped_angle, 20)
                    time.sleep(0.5)
                
                time.sleep(1)  # 상태 간의 대기 시간
            print(f"One cycle completed")
        print(f"Repeated {repeat_count} times")

if __name__ == '__main__':
    # 카메라 스레드를 데몬 스레드로 설정
    camera_thread = threading.Thread(target=start_camera)
    camera_thread.daemon = True
    camera_thread.start()

    # PyQt5 GUI 스레드 시작
    app = QApplication(sys.argv)
    window = MyCobotController()
    window.show()
    sys.exit(app.exec_())
