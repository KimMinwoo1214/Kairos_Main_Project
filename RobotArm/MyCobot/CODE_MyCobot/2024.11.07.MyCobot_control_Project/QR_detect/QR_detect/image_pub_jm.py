import sys
import cv2
import time
from pyzbar import pyzbar
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal
from pymycobot import MyCobot
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class CameraThread(QThread):
    frame_captured = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.cap = None  # 카메라 객체를 인스턴스 변수로 초기화
        self.active = True  # 카메라 활성 상태를 추적하는 플래그

    def run(self):
        self.cap = cv2.VideoCapture(0, cv2.CAP_V4L)

        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            return

        while self.active:  # 카메라가 활성 상태일 때만 실행
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to grab frame")
                break
            self.frame_captured.emit(frame)  # 캡처한 프레임을 시그널로 전송
            time.sleep(0.1)  # 프레임 캡처 속도 조절

    def stop(self):
        self.active = False  # 카메라 비활성화
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()


class QRCodePublisher(Node):
    def __init__(self):
        super().__init__('qr_code_publisher')
        self.publisher_ = self.create_publisher(Image, 'qr_code_image', 10)
        self.bridge = CvBridge()

    def publish_image(self, frame):
        # OpenCV 프레임을 ROS 이미지 메시지로 변환
        img_msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.publisher_.publish(img_msg)


class ROS2Thread(QThread):
    def __init__(self, node):
        super().__init__()
        self.node = node
        self.running = True

    def run(self):
        while rclpy.ok() and self.running:
            rclpy.spin_once(self.node, timeout_sec=0.1)  # Non-blocking 방식으로 spin

    def stop(self):
        self.running = False  # 스레드 종료 시 플래그 False로 설정
        self.node.destroy_node()  # 노드 파괴
        rclpy.shutdown()  # ROS2 종료


class MyCobotController(QWidget):
    def __init__(self):
        super().__init__()
        self.mc = MyCobot('/dev/ttyACM0', 115200)
        self.joint_ranges = [(-165, 165), (-165, 165), (-165, 165), (-165, 165), (-165, 165), (-175, 175)]
        self.gripper_state = None

        # 그리퍼 초기화 및 캘리브레이션
        self.mc.set_gripper_mode(0)  # 그리퍼 모드 설정
        self.mc.set_gripper_calibration()  # 그리퍼 캘리브레이션 수행
        self.mc.init_gripper()  # 그리퍼 초기화
        print("Gripper calibration and initialization complete.")

        self.qr_code_publisher = QRCodePublisher()  # QR 코드 퍼블리셔 초기화
        self.ros2_thread = ROS2Thread(self.qr_code_publisher)  # ROS 2 스핀을 위한 스레드 초기화
        self.ros2_thread.start()
        self.camera_thread = CameraThread()  # 카메라 스레드를 인스턴스 변수로 초기화
        self.camera_thread.frame_captured.connect(self.process_frame)  # QR 코드 인식 시 처리
        self.initUI()

        self.qr_detected = False  # QR 코드 인식 여부 플래그

    def initUI(self):
        self.setWindowTitle('MyCobot Control')
        self.setGeometry(100, 100, 300, 300)

        vbox = QVBoxLayout()

        scenario_button = QPushButton('Execute Scenario')
        scenario_button.clicked.connect(self.execute_scenario)
        vbox.addWidget(scenario_button)

        self.setLayout(vbox)

    def closeEvent(self, event):
        """GUI 창이 닫힐 때 모든 스레드를 종료합니다."""
        print("Closing application...")
        self.camera_thread.stop()  # 카메라 스레드 종료
        self.ros2_thread.stop()  # ROS2 스레드 종료
        rclpy.shutdown()  # ROS2 시스템 종료
        event.accept()

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
        print("Starting scenario...")
        self.move_to_position([0, 0, 0, 0, 0, 0], 5)
        print("Moved to initial position.")

        self.move_to_position([0, -59, -54, 31.7, 90.7, 0], 5)
        print("Moved to QR code detection position.")

        # QR 코드 인식을 위해 카메라 시작
        self.qr_detected = False
        self.camera_thread.active = True  # 카메라 활성화
        self.camera_thread.start()
        print("Camera started for QR code detection.")

        # QR 코드가 감지될 때까지 무한 대기
        while not self.qr_detected:
            time.sleep(0.1)

        self.camera_thread.stop()
        print("Camera stopped and released.") 

        # QR 코드가 감지된 후에 다음 작업 진행
        print("Moving to next position...")   
        self.move_to_position([0, -75.2, -39.6, 33.3, 89, 0], 5)
        print("Moved to pick-up position.")
        time.sleep(3)
        self.close_gripper()
        time.sleep(3)
        self.move_to_position([0, 0, 0, 0, 0, 0], 5)
        self.move_to_position([-91.1, -78.1, 0, 0, 0, 0], 5)
        time.sleep(3)
        self.open_gripper()
        time.sleep(3)
        self.move_to_position([0, 0, 0, 0, 0, 0], 5)
        print("Scenario execution completed.")

    def process_frame(self, frame):
        if not self.qr_detected:  # QR 코드가 아직 감지되지 않은 경우에만 수행
            # QR 코드 인식
            decoded_objects = pyzbar.decode(frame)
            if decoded_objects:
                self.qr_detected = True  # QR 코드가 인식되면 플래그 설정
                for obj in decoded_objects:
                    qr_data = obj.data.decode("utf-8")
                    print("QR Code detected:", qr_data)
                    # QR 코드 이미지 퍼블리시
                    self.qr_code_publisher.publish_image(frame)
                    break  # 첫 번째 QR 코드만 처리

                # QR 코드가 인식되면 카메라 종료
                self.camera_thread.stop()
                print("QR Code detected and camera stopped.")


def main(args=None):
    rclpy.init(args=args)
    app = QApplication(sys.argv)
    window = MyCobotController()
    window.show()

    try:
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        print("Shutting down.")
    finally:
        window.camera_thread.stop()  # 카메라 스레드 종료
        rclpy.shutdown()  # ROS2 종료


if __name__ == '__main__':
    main()