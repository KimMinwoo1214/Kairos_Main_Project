#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import cv2
import imutils
import socket
import numpy as np
import time
import base64
from pyzbar import pyzbar
from std_msgs.msg import String

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

class UdpVideoServer(Node):
    def __init__(self):
        super().__init__('udp_video_server')
        
        # Initialize socket
        self.BUFF_SIZE = 65536
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.BUFF_SIZE)
        
        # Define host and port
        self.host_ip = '192.168.0.137'
        self.port = 9090
        self.socket_address = (self.host_ip, self.port)
        
        # Bind socket
        self.server_socket.bind(self.socket_address)
        self.get_logger().info(f'Listening at: {self.socket_address}')
        
        # Initialize video capture
        self.vid = cv2.VideoCapture(1)
        if not self.vid.isOpened():
            self.get_logger().error("Error: Could not open video device")
            exit()
        
        # Publisher for QR code data
        self.qr_publisher = self.create_publisher(String, 'qr_code_data', 10)

        # FPS and frame counter variables
        self.fps, self.st, self.frames_to_count, self.cnt = (0, 0, 20, 0)

        # Main loop for the video server
        self.run_server()

    def run_server(self):
        WIDTH = 400
        while True:
            # Wait for client message
            msg, client_addr = self.server_socket.recvfrom(self.BUFF_SIZE)
            self.get_logger().info(f'GOT connection from {client_addr}')

            while self.vid.isOpened():
                ret, frame = self.vid.read()
                if not ret:
                    self.get_logger().error("Failed to capture image")
                    break
                
                # Resize and encode frame
                frame = imutils.resize(frame, width=WIDTH)
                
                # QR 코드 인식
                decoded_objects = pyzbar.decode(frame)
                for obj in decoded_objects:
                    qr_data = obj.data.decode("utf-8")
                    if qr_data in QR_CODES:
                        # 퍼블리시할 QR 코드 메시지 생성 및 퍼블리시
                        msg = String()
                        msg.data = QR_CODES[qr_data]
                        self.qr_publisher.publish(msg)
                        self.get_logger().info(f"Published QR Code data: {QR_CODES[qr_data]}")
                    
                    # QR 코드 위치에 사각형 그리기
                    points = obj.polygon
                    if len(points) == 4:
                        pts = np.array([[p.x, p.y] for p in points], np.int32)
                        pts = pts.reshape((-1, 1, 2))
                        cv2.polylines(frame, [pts], True, (0, 0, 255), 3)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.putText(frame, qr_data, (points[0].x, points[0].y - 10), font, 0.9, (0, 0, 255), 2)
                
                # Encode and send frame
                encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
                message = base64.b64encode(buffer)
                self.server_socket.sendto(message, client_addr)
                
                # Calculate FPS
                if self.cnt == self.frames_to_count:
                    try:
                        self.fps = round(self.frames_to_count / (time.time() - self.st))
                        self.st = time.time()
                        self.cnt = 0
                    except ZeroDivisionError:
                        pass
                self.cnt += 1


def main(args=None):
    rclpy.init(args=args)
    node = UdpVideoServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.vid.release()
        node.server_socket.close()
        node.get_logger().info("Shutting down server.")
        rclpy.shutdown()


if __name__ == '__main__':
    main()
