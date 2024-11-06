import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from pyzbar import pyzbar
import cv2
import numpy as np

# QR 코드 데이터 사전
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
    "3-4": "과학4 - 과학 - 4",
    "4-4": "예술4 - 예술 - 4",
}

class QRCodeSubscriber(Node):
    def __init__(self):
        super().__init__('qr_code_subscriber')
        self.subscription = self.create_subscription(Image, 'qr_code_image', self.listener_callback, 10)
        self.bridge = CvBridge()

    def listener_callback(self, msg):
        # ROS 메시지를 OpenCV 이미지로 변환
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        # QR 코드 인식
        decoded_objects = pyzbar.decode(frame)
        for obj in decoded_objects:
            qr_data = obj.data.decode("utf-8")
            
            # QR 코드 위치에 사각형 그리기
            points = obj.polygon
            if len(points) == 4:
                pts = np.array([[p.x, p.y] for p in points], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
            
            # QR 코드 데이터 화면에 표시
            text = QR_CODES.get(qr_data, "Unknown QR Code")
            cv2.putText(frame, text, (obj.rect.left, obj.rect.top - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)


            print(f"QR Code detected: {qr_data}")
            if qr_data in QR_CODES:
                print(f"Matched Data: {QR_CODES[qr_data]}")
            else:
                print("No matching data found.")
        
        # 카메라 영상 화면에 표시
        cv2.imshow("Camera Feed", frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    qr_code_subscriber = QRCodeSubscriber()
    rclpy.spin(qr_code_subscriber)
    rclpy.shutdown()
    cv2.destroyAllWindows()  # 프로그램 종료 시 모든 창 닫기

if __name__ == '__main__':
    main()
