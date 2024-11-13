#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import cv2
import imutils
import socket
import numpy as np
import time
import base64

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
        self.vid = cv2.VideoCapture(0)
        if not self.vid.isOpened():
            self.get_logger().error("Error: Could not open video device")
            exit()
        
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
                _, frame = self.vid.read()
                if frame is None:
                    self.get_logger().error("Failed to capture image")
                    break
                
                # Resize and encode frame
                frame = imutils.resize(frame, width=WIDTH)
                encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
                message = base64.b64encode(buffer)
                
                # Send encoded frame over UDP
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