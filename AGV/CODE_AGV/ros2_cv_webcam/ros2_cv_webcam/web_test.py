#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import imutils
import socket
import numpy as np
import base64
import time

class UdpVideoServer(Node):
    def __init__(self):
        super().__init__('udp_video_server')
        
        # Initialize socket
        self.BUFF_SIZE = 65536
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.BUFF_SIZE)
        
        # Define host and port
        self.host_ip = '192.168.0.137'  # Replace with the actual server IP
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
        
        # ROS2 publisher for camera images
        self.image_pub = self.create_publisher(Image, '/image_raw', 10)
        self.bridge = CvBridge()  # CvBridge instance for converting OpenCV images to ROS2 Image messages
        
        # FPS and frame counter variables
        self.fps, self.st, self.frames_to_count, self.cnt = (0, 0, 20, 0)

        # Main loop for the video server
        self.run_server()

    def run_server(self):
        WIDTH = 400
        while True:
            try:
                # Wait for client message
                try:
                    msg, client_addr = self.server_socket.recvfrom(self.BUFF_SIZE)
                    self.get_logger().info(f"Received raw message from {client_addr}: {msg}")
                except socket.timeout:
                    self.get_logger().warn("No client message received: waiting...")
                    continue

                # Decode and check message
                decoded_msg = msg.decode('utf-8', errors='ignore').strip()
                if decoded_msg == '1':
                    self.get_logger().info(f"Detection confirmed from {client_addr}")
                elif decoded_msg == '0':
                    self.get_logger().info(f"No detection from {client_addr}")

                # Capture and send video frames to the client
                ret, frame = self.vid.read()
                if not ret:
                    self.get_logger().error("Failed to capture image")
                    break
                
                # Resize and encode frame
                frame = imutils.resize(frame, width=WIDTH)
                
                # Publish frame to ROS2 topic
                ros_image = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
                self.image_pub.publish(ros_image)
                self.get_logger().info("Published frame to /image_raw")

                # Encode frame for UDP transmission
                encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 60])  # Lower quality to save bandwidth
                message = base64.b64encode(buffer)
                
                # Check if the message size is appropriate
                if len(message) > self.BUFF_SIZE:
                    self.get_logger().warn("Frame size exceeds buffer, dropping frame")
                    continue
                
                # Send encoded frame over UDP
                self.get_logger().info(f"Sending packet to {client_addr}, packet size: {len(message)} bytes")
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

            except socket.error as e:
                self.get_logger().error(f"Socket error: {e}")
                break

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