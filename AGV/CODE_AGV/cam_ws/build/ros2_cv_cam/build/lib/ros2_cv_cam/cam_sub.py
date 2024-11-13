#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32, Int32, Float32MultiArray
import cv2
import socket
import numpy as np
import base64
from ultralytics import YOLO  # YOLOv8 model loading
import warnings

warnings.filterwarnings("ignore", category=UserWarning, message="Unable to import Axes3D")

class UdpVideoYOLONode(Node):
    def __init__(self):
        super().__init__('udp_video_yolo_node')
        
        # ROS2 Publishers for detection results
        self.bbox_pub = self.create_publisher(Float32MultiArray, '/BBox', 10)
        self.class_id_pub = self.create_publisher(Int32, '/class_id', 10)
        self.class_name_pub = self.create_publisher(String, '/class_name', 10)
        self.score_pub = self.create_publisher(Float32, '/score', 10)
        
        self.BUFF_SIZE = 65536
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.BUFF_SIZE)
        
        self.host_ip = '192.168.0.137'  # Video server IP
        self.port = 9090
        self.server_address = (self.host_ip, self.port)
        
        try:
            self.client_socket.sendto(b'Hello', self.server_address)
            self.get_logger().info(f"Initial connection message sent to {self.server_address}")
        except socket.error as e:
            self.get_logger().error(f"Failed to send initial message: {e}")
        
        self.model = YOLO('/home/kmw/best.pt')  # Update path to your YOLO model
        self.run_client()

    def run_client(self):
        while rclpy.ok():
            try:
                packet, _ = self.client_socket.recvfrom(self.BUFF_SIZE)
                self.get_logger().info("Received packet from video server.")

                try:
                    data = base64.b64decode(packet, ' /')
                    npdata = np.frombuffer(data, dtype=np.uint8)
                    frame = cv2.imdecode(npdata, 1)
                    if frame is None:
                        raise ValueError("Frame decoding failed.")
                except Exception as e:
                    self.get_logger().error(f"Error decoding frame: {e}")
                    continue

                try:
                    results = self.model(frame)

                    for box in results[0].boxes:
                        conf = box.conf[0]
                        if conf >= 0.7:  # Confidence threshold for drawing the bounding box
                            x1, y1, x2, y2 = [float(coord) for coord in box.xyxy[0]]  # float으로 변환
                            cls = int(box.cls[0])
                            label = results[0].names[cls]

                            # Draw the bounding box and label
                            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                            cv2.putText(frame, f"{label} {conf:.2f}", (int(x1), int(y1) - 10), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                            # Publish detection results
                            bbox_msg = Float32MultiArray(data=[x1, y1, x2, y2])
                            self.bbox_pub.publish(bbox_msg)

                            class_id_msg = Int32(data=cls)
                            self.class_id_pub.publish(class_id_msg)

                            class_name_msg = String(data=label)
                            self.class_name_pub.publish(class_name_msg)

                            score_msg = Float32(data=float(conf))  # float으로 변환
                            self.score_pub.publish(score_msg)

                except Exception as e:
                    self.get_logger().error(f"Error during YOLO detection: {e}")
                    continue

                # Display the processed frame with bounding boxes
                cv2.imshow("YOLOv8 Detection", frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    self.client_socket.close()
                    cv2.destroyAllWindows()
                    break

            except Exception as e:
                self.get_logger().error(f"Error in main loop: {e}")
                continue

def main(args=None):
    rclpy.init(args=args)
    node = UdpVideoYOLONode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.client_socket.close()
        cv2.destroyAllWindows()
        node.get_logger().info("Shutting down node.")
        rclpy.shutdown()

if __name__ == '__main__':
    main()
