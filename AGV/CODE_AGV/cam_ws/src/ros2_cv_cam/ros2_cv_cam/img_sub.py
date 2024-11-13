#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import cv2
import socket
import numpy as np
import time
import base64

class UdpVideoClient(Node):
    def __init__(self):
        super().__init__('udp_video_client')
        
        # Set up socket for UDP communication
        self.BUFF_SIZE = 65536
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.BUFF_SIZE)
        
        # Define server address
        self.host_ip = '192.168.0.137'  # replace with the actual server IP if different
        self.port = 9090
        self.server_address = (self.host_ip, self.port)
        
        # Send initial connection message to server
        self.message = b'Hello'
        self.client_socket.sendto(self.message, self.server_address)
        
        # Initialize frame counter and FPS calculation variables
        self.fps, self.st, self.frames_to_count, self.cnt = (0, 0, 20, 0)

        # Start receiving video frames
        self.run_client()

    def run_client(self):
        while True:
            # Receive packet from server
            packet, _ = self.client_socket.recvfrom(self.BUFF_SIZE)
            
            # Decode the base64 data
            data = base64.b64decode(packet, ' /')
            npdata = np.frombuffer(data, dtype=np.uint8)
            
            # Decode image frame from numpy array
            frame = cv2.imdecode(npdata, 1)
            frame = cv2.putText(frame, f'FPS: {self.fps}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            
            # Display the frame
            cv2.imshow("RECEIVING VIDEO", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                self.client_socket.close()
                cv2.destroyAllWindows()
                break
            
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
    node = UdpVideoClient()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.client_socket.close()
        cv2.destroyAllWindows()
        node.get_logger().info("Shutting down client.")
        rclpy.shutdown()


if __name__ == '__main__':
    main()
