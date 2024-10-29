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
    # 0은 기본 카메라를 의미, 여러 대의 카메라가 연결되어 있다면 다른 번호를 시도
    cap = cv2.VideoCapture(0)  # 카메라 시작

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # 카메라에서 프레임 읽기
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # 화면에 프레임 표시
        cv2.imshow('MyCobot Camera', frame)

        # 'q'를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 카메라 해제 및 창 닫기
    cap.release()
    cv2.destroyAllWindows()

class MyCobotController(QWidget):
    def __init__(self):
        super().__init__()

        # MyCobot 연결 설정
        self.mc = MyCobot('COM3', 115200)

        # 각 조인트의 각도 범위 설정
        self.joint_ranges = [
            (-160, 160),  # 1번 조인트
            (-85, 90),    # 2번 조인트
            (-180, 45),   # 3번 조인트
            (-160, 160),  # 4번 조인트
            (-100, 100),  # 5번 조인트
            (-180, 180),  # 6번 조인트
        ]

        self.mc.set_gripper_mode(0)
        
        self.joint_angles = [0, 0, 0, 0, 0, 0]  # 초기 각도 설정
        self.gripper_state = None  # 그리퍼 상태 (1: 열기, 0: 닫기)
        self.saved_states = []  # 저장된 각도 및 그리퍼 상태
        
        # 경로 입력 필드
        self.filepath_input = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MyCobot Real-time Angle and Coordinates Display with Gripper Control')
        self.setGeometry(100, 100, 400, 700)  # 윈도우 크기 확대

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

        # 그리퍼 제어 버튼 추가
        gripper_hbox = QHBoxLayout()
        
        self.gripper_open_button = QPushButton('Close Gripper')
        self.gripper_open_button.clicked.connect(self.open_gripper)
        gripper_hbox.addWidget(self.gripper_open_button)

        self.gripper_close_button = QPushButton('Open Gripper')
        self.gripper_close_button.clicked.connect(self.close_gripper)
        gripper_hbox.addWidget(self.gripper_close_button)

        vbox.addLayout(gripper_hbox)

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
        self.mc.send_angle(joint_index + 1, value, 20)

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
        
        # 좌표도 초기화
        self.coords_label.setText('Coordinates (x, y, z, rx, ry, rz): (0, 0, 0, 0, 0, 0)')

    def open_gripper(self):
        # 그리퍼 열기 (속도 50)
        self.mc.set_gripper_state(1, 50)  # 1: 열기, 50: 중간 속도
        self.gripper_state = 1  # 그리퍼 상태 저장
        print("Gripper opened.")

    def close_gripper(self):
        # 그리퍼 닫기 (속도 50)
        self.mc.set_gripper_state(0, 50)  # 0: 닫기, 50: 중간 속도
        self.gripper_state = 0  # 그리퍼 상태 저장
        print("Gripper closed.")

    def save_image(self):
        """ 카메라에서 현재 프레임을 캡처하고 이미지를 저장 """
        global cap, i
        filepath = self.filepath_input.text().strip()  # 입력된 경로

        if cap is not None and filepath:
            ret, frame = cap.read()
            if ret:
                # timestamp = time.strftime("%Y%m%d_%H%M%S")
                filename = f"{filepath}/Red_{i}.png"
                cv2.imwrite(filename, frame)
                print(f"Image saved as {filename}")
                i += 1  # 다음 이미지를 위한 인덱스 증가
            else:
                print("Failed to capture image")
        else:
            print("Camera not initialized or file path not set")
    
    def save_current_position(self):
        # 현재 각도와 그리퍼 상태를 저장
        state = {
            'angles': self.joint_angles.copy(),
            'gripper': self.gripper_state
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
                    self.mc.send_angle(i + 1, angle, 20)
                    time.sleep(0.5)

                # 각 관절 움직임 완료 후 그리퍼 상태 복원
                if state['gripper'] == 1:
                    self.mc.set_gripper_state(1, 50)  # 그리퍼 열기
                else:
                    self.mc.set_gripper_state(0, 50)  # 그리퍼 닫기
                
                time.sleep(1)  # 상태 간의 대기 시간
            print(f"One cycle completed")
        print(f"Repeated {repeat_count} times")

if __name__ == '__main__':
    # 카메라 스레드를 데몬 스레드로 설정
    camera_thread = threading.Thread(target=start_camera)
    camera_thread.daemon = True  # 데몬 스레드로 설정
    camera_thread.start()

    # PyQt5 GUI 스레드 시작
    app = QApplication(sys.argv)
    window = MyCobotController()
    window.show()
    sys.exit(app.exec_())