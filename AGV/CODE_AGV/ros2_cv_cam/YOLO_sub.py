#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # For sending detection messages
import cv2
import socket
import numpy as np
import base64
from ultralytics import YOLO  # YOLOv8 model loading
import warnings

# Suppress specific warnings from Matplotlib if they appear
warnings.filterwarnings("ignore", category=UserWarning, message="Unable to import Axes3D")

class UdpVideoYOLOClient(Node):
    def __init__(self):
        super().__init__('udp_video_yolo_client')

        # Set up socket for UDP communication
        self.BUFF_SIZE = 65536
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.BUFF_SIZE)

        # Define server address
        self.host_ip = '192.168.0.137'  # Replace with actual server IP if different
        self.port = 9090
        self.server_address = (self.host_ip, self.port)

        # Send initial connection message to server
        self.message = b'Hello'
        self.client_socket.sendto(self.message, self.server_address)

        # YOLOv8 model initialization
        self.model = YOLO('/home/kmw/best.pt')  # Update path to your YOLOv8 model

        # Publisher for detection messages
        self.detection_publisher = self.create_publisher(String, 'detection_status', 10)

        # Start receiving and processing video frames
        self.run_client()

    def run_client(self):
        while True:
            # Receive packet from server
            packet, _ = self.client_socket.recvfrom(self.BUFF_SIZE)

            # Decode the base64 data to an image
            data = base64.b64decode(packet, ' /')
            npdata = np.frombuffer(data, dtype=np.uint8)
            frame = cv2.imdecode(npdata, 1)

            # Perform YOLOv8 detection on the frame
            results = self.model(frame)
            detection_occurred = False  # Track if any detection occurred

            # Draw bounding boxes on detected objects
            for box in results[0].boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box coordinates as integers
                conf = box.conf[0]  # Confidence score
                cls = int(box.cls[0])  # Class index, converted to integer
                label = f"{results[0].names[cls]} {conf:.2f}"
                # Draw bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                detection_occurred = True

            # Publish a message if a detection occurred
            if detection_occurred:
                detection_msg = String()
                detection_msg.data = "Detection complete"
                self.detection_publisher.publish(detection_msg)

            # Display the processed frame with bounding boxes
            cv2.imshow("YOLOv8 Detection", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                self.client_socket.close()
                cv2.destroyAllWindows()
                break

def main(args=None):
    rclpy.init(args=args)
    node = UdpVideoYOLOClient()
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