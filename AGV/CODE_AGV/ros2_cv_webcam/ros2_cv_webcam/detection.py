#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import socket

class DetectionStatusReceiver(Node):
    def __init__(self):
        super().__init__('detection_status_receiver')

        # Initialize socket for receiving status messages
        self.BUFF_SIZE = 1024
        self.status_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.status_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.BUFF_SIZE)

        # Define host and port for this receiver
        self.host_ip = '192.168.0.137'  # Replace with your IP
        self.port = 9091  # Use a different port for this node
        self.socket_address = (self.host_ip, self.port)

        # Bind socket
        self.status_socket.bind(self.socket_address)
        self.get_logger().info(f'Listening for status messages at: {self.socket_address}')

        # Start receiving loop
        self.run_receiver()

    def run_receiver(self):
        while True:
            try:
                # Receive status message
                msg, client_addr = self.status_socket.recvfrom(self.BUFF_SIZE)
                decoded_msg = msg.decode('utf-8').strip()

                # Log the received status
                if decoded_msg == '1':
                    self.get_logger().info(f"Detection!!! {client_addr}")
                elif decoded_msg == '0':
                    self.get_logger().info(f"No detection from {client_addr}")
                else:
                    self.get_logger().warn(f"Unexpected message received: {decoded_msg}")

            except socket.error as e:
                self.get_logger().error(f"Socket error: {e}")
                break

def main(args=None):
    rclpy.init(args=args)
    node = DetectionStatusReceiver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.status_socket.close()
        node.get_logger().info("Shutting down status receiver.")
        rclpy.shutdown()

if __name__ == '__main__':
    main()
