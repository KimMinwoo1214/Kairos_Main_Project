import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import cv2
import numpy as np
import math
import time

class LineTracingPublisher(Node):
    def __init__(self):
        super().__init__('line_tracing_publisher')
        self.publisher_ = self.create_publisher(String, 'agv_direction', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  # 10Hz
        self.cap = cv2.VideoCapture(1)

        if not self.cap.isOpened():
            self.get_logger().error("Cannot open camera.")

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warning("Cannot receive frame.")
            return

        height, width = frame.shape[:2]
        center_y = int(height * 0.7)

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv = cv2.GaussianBlur(hsv, (5, 5), 0)

        # Define yellow color range in HSV
        lower_yellow = np.array([15, 100, 100])
        upper_yellow = np.array([35, 255, 255])

        # Create yellow mask
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # Edge detection using Canny
        edges = cv2.Canny(mask, 50, 200, apertureSize=3)

        # Hough Transform to detect lines
        lines = cv2.HoughLinesP(edges, 1, math.pi/180, threshold=30, minLineLength=30, maxLineGap=10)

        direction = "stopped"
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                if (y1 < center_y and y2 > center_y) or (y1 > center_y and y2 < center_y):
                    angle_rad = math.atan2(y2 - y1, x2 - x1)
                    angle_deg = math.degrees(angle_rad)

                    if (-90 <= angle_deg <= -45) or (45 <= angle_deg <= 90):
                        direction = "forward"
                    elif (0 <= angle_deg < 45):
                        direction = "ccw"
                    elif (-45 <= angle_deg < 0):
                        direction = "cw"
                    break

        msg = String()
        msg.data = direction
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing direction: {direction}')

    def destroy_node(self):
        super().destroy_node()
        if self.cap.isOpened():
            self.cap.release()


def main(args=None):
    rclpy.init(args=args)
    line_tracing_publisher = LineTracingPublisher()
    rclpy.spin(line_tracing_publisher)
    line_tracing_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

# launch file (line_tracing_launch.py)
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='agv_line_tracing',
            executable='line_tracing_publisher',
            name='line_tracing_publisher',
            output='screen'
        ),
        Node(
            package='agv_line_tracing',
            executable='agv_control_subscriber',
            name='agv_control_subscriber',
            output='screen'
        ),
    ])

