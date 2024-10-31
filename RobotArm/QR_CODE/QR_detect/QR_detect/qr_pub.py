import rclpy 
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
from pyzbar import pyzbar

# QR 코드 데이터 매핑
QR_CODES = {
    "1-1": "돈 버는 법 - 경제 - 1",
    "2-1": "채식주의자 - 소설 - 1",
    "3-1": "Thermal Dynamics - 과학 - 1",
    "4-1": "책으로 보는 고흐 - 예술 - 1",
    "1-2": "주식으로 돈 벌기 - 경제 - 2",
    "2-2": "데미안 - 소설 - 2",
    "3-2": "일반물리학 - 과학 - 2",
    "4-2": "만화로 보는 국악 - 예술 - 2",
    "1-3": "경제3 - 경제 - 3",
    "2-3": "운수 좋은 날 - 소설 - 3",
    "3-3": "COSMOS - 과학 - 3",
    "4-3": "피아노 - 예술 - 3",
    "1-4": "나스닥 - 경제 - 4",
    "2-4": "호밀밭의 파수꾼 - 소설 - 4",
    "3-4": "과학4 - 과학- 4",
    "4-4": "예술4 - 예술 - 4",
}

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')  # Node name
        self.subscription = self.create_subscription(
            Image,  # Message type
            'video_frames',  # Topic name
            self.listener_callback,
            10)
        self.br = CvBridge()

    def listener_callback(self, data):
        # ROS 로그로 수신 확인
        self.get_logger().info('Receiving Video frame')

        # ROS Image 메시지를 OpenCV 이미지로 변환
        current_frame = self.br.imgmsg_to_cv2(data)

        # QR 코드 인식
        decoded_frame = self.decode_qr(current_frame)

        # 결과 프레임 화면에 표시
        cv2.imshow("QR Code Scanner", decoded_frame)
        cv2.waitKey(1)

    def decode_qr(self, frame):
        # 프레임에서 QR 코드 디코딩
        decoded_objects = pyzbar.decode(frame)
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            if qr_data in QR_CODES:
                self.get_logger().info(f"QR Code Recognized: {QR_CODES[qr_data]}")
            else:
                self.get_logger().warning(f"Unknown QR code: {qr_data}")
            
            # QR 코드 주변에 사각형 그리기
            (x, y, w, h) = obj.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # QR 코드 데이터 표시
            cv2.putText(frame, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)
        
        return frame

def main():
    rclpy.init()  # ROS 통신 시작
    image_subscriber = ImageSubscriber()  # 클래스 생성
    rclpy.spin(image_subscriber)
    image_subscriber.destroy_node()

    rclpy.shutdown()  # ROS 통신 종료


if __name__ == '__main__':
    main()
