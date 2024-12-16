#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
from pyzbar import pyzbar

# QR 코드 데이터 매핑
QR_CODES = {
    "CW": 'Clock Wise Rotation',
    "CCW": 'Counter Clock Wise Rotation',
}

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')  # 노드 이름 설정
        self.subscription = self.create_subscription(
            Image,  # 메시지 타입
            'video_frames',  # 토픽 이름
            self.listener_callback,
            10)
        self.br = CvBridge()

        # teleop_commands 토픽에 대한 퍼블리셔 생성
        self.command_publisher = self.create_publisher(String, 'teleop_commands', 10)

    def listener_callback(self, data):
        # ROS 로그로 수신 확인
        self.get_logger().info('비디오 프레임 수신 중')

        # ROS Image 메시지를 OpenCV 이미지로 변환
        current_frame = self.br.imgmsg_to_cv2(data)

        # QR 코드 인식
        decoded_frame = self.decode_qr(current_frame)

        # 결과 프레임 화면에 표시
        cv2.imshow("QR 코드 스캐너", decoded_frame)
        cv2.waitKey(1)

    def decode_qr(self, frame):
        # 프레임에서 QR 코드 디코딩
        decoded_objects = pyzbar.decode(frame)
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            if qr_data in QR_CODES:
                self.get_logger().info(f"QR 코드 인식됨: {QR_CODES[qr_data]}")

                # QR 코드에 따라 명령 생성 및 퍼블리시
                command_msg = String()
                if qr_data == "CW":
                    command_msg.data = "cw"
                elif qr_data == "CCW":
                    command_msg.data = "ccw"
                else:
                    command_msg.data = "stop"
                self.command_publisher.publish(command_msg)
            else:
                self.get_logger().warning(f"알 수 없는 QR 코드: {qr_data}")

            # QR 코드 주변에 사각형 그리기
            (x, y, w, h) = obj.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # QR 코드 데이터 표시
            cv2.putText(frame, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)

        return frame

def main():
    rclpy.init()  # ROS 통신 시작
    image_subscriber = ImageSubscriber()  # 클래스 인스턴스 생성
    rclpy.spin(image_subscriber)
    image_subscriber.destroy_node()

    rclpy.shutdown()  # ROS 통신 종료

if __name__ == '__main__':
    main()

