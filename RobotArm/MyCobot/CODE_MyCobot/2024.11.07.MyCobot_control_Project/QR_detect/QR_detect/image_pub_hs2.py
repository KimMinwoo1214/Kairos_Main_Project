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

    def run(self):
        self.cap = cv2.VideoCapture(0, cv2.CAP_V4L)
        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            return

        # while True:
        #     ret, frame = self.cap.read()
        #     if not ret:
        #         print("Failed to grab frame2")
        #         break
        #     self.frame_captured.emit(frame)  # 캡처한 프레임을 시그널로 전송
        #     time.sleep(0.1)  # 프레임 캡처 속도 조절

    def stop(self):
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()


class QRCodePublisher(Node):
    def __init__(self):
        super().__init__('qr_code_publisher')
        self.publisher_ = self.create_publisher(Image, 'qr_code_image', 10)
        self.bridge = CvBridge()

    def publish_image(self, frame):
        img_msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.publisher_.publish(img_msg)
        self.get_logger().info("Publishing image with QR code.")


# class ROS2Thread(QThread):
#     def __init__(self, node):
#         super().__init__()
#         self.node = node
#         self.running = True

#     def run(self):
#         while rclpy.ok() and self.running:
#             rclpy.spin_once(self.node, timeout_sec=0.1)

#     def stop(self):
#         self.running = False
#         self.node.destroy_node()
#         rclpy.shutdown()


class MyCobotController(QWidget):
    def __init__(self):
        super().__init__()
        self.mc = MyCobot('/dev/ttyACM0', 115200)
        self.joint_ranges = [(-165, 165), (-165, 165), (-165, 165), (-165, 165), (-165, 165), (-175, 175)]
        self.gripper_state = None
        self.qr_code_publisher = QRCodePublisher()
        # self.ros2_thread = ROS2Thread(self.qr_code_publisher)
        # self.ros2_thread.start()
        self.camera_thread = CameraThread()
        # self.camera_thread.frame_captured.connect(self.qr_code_publisher.publish_image)
        self.qr_recognized = False  # QR 코드 인식 여부 플래그
        self.last_recognition_time = time.time()
        self.timeout = 10  # QR 코드 인식 타임아웃
        self.initUI()

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
        # self.ros2_thread.stop()  # ROS2 스레드 종료
        # rclpy.shutdown()  # ROS2 종료
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

        self.qr_recognized = False
        
        print("Starting scenario...")
        self.move_to_position([0, 0, 0, 0, 0, 0], 5)
        print("Moved to initial position.")
 

        self.move_to_position([0, -59, -54, 31.7, 90.7, 0], 5)
        print("Searching for QR code...")

        # 카메라를 시작하고 QR 코드 인식 대기
        self.camera_thread.start()
        print("Camera started for QR code detection.")
        time.sleep(0.2)

        

        # QR 코드 탐지 루프에 타임아웃 설정
        start_time = time.time()  # 현재 시간을 저장

        while True:
            # 타임아웃 확인
            if time.time() - start_time > self.timeout:
                print("QR code detection timed out.")
                break

            ret, frame = self.camera_thread.cap.read()

            if not ret:
                print("Failed to grab frame1")
                break  # 카메라 읽기 실패 시 루프 종료

            # QR 코드 탐지 시, 첫 번째 QR 코드만 퍼블리싱
            if self.detect_qr_code(frame):  # QR 코드가 발견되면
                if not self.qr_recognized:  # 첫 번째 QR 코드일 때만 퍼블리시
                    print("QR Code detected.")
                    self.qr_code_publisher.publish_image(frame)  # 이미지 퍼블리시
                    self.qr_recognized = True  # QR 코드가 인식되었음을 표시
                break  # QR 코드 발견 후 종료

            time.sleep(1)  # 계속해서 QR 코드 탐지 시도

        self.camera_thread.stop()  # 시나리오 종료 후 카메라 스레드 종료
        print("Camera stopped and released.")

        # 지연 후 다음 동작
        time.sleep(1)
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

        # 시나리오가 끝난 후 QR 코드 퍼블리싱을 계속 할 수 있도록 플래그 리셋
        self.qr_recognized = False

    def detect_qr_code(self, frame):
        decoded_objects = pyzbar.decode(frame)
        if decoded_objects:  # QR 코드가 하나라도 발견되면
            for obj in decoded_objects:
                print("QR Code detected:", obj.data.decode("utf-8"))  # QR 코드 값 출력
            return True
        return False  # QR 코드가 없으면 False 반환


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
        window.camera_thread.stop()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
