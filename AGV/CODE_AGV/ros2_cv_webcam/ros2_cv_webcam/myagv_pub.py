# Import ROS2-related libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import cv2
import numpy as np
import math

class CameraProcessorNode(Node):
    def __init__(self):
        super().__init__('camera_processor_node')
        # Publisher to send commands to wheel command node
        self.publisher_ = self.create_publisher(String, 'wheel_command', 10)
        self.timer = self.create_timer(0.1, self.calculate_yellow_line_angle_live)
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.get_logger().error('Cannot open camera.')
        
    def calculate_yellow_line_angle_live(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warn('Cannot receive frame.')
            return

        output = frame.copy()
        height, width = frame.shape[:2]
        center_y = int(height * 0.7)

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv = cv2.GaussianBlur(hsv, (5, 5), 0)

        # Define yellow color range in HSV
        lower_yellow = np.array([15, 100, 100])
        upper_yellow = np.array([35, 255, 255])

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
        mask = cv2.dilate(mask, kernel, iterations=1)

        edges = cv2.Canny(mask, 50, 200, apertureSize=3)
        lines = cv2.HoughLinesP(edges, 1, math.pi/180, threshold=30, minLineLength=30, maxLineGap=10)

        direction = 'stop'  # Default to stop if no line is detected

        if lines is not None:
            lines = sorted(lines, key=lambda line: math.hypot(line[0][2] - line[0][0], line[0][3] - line[0][1]), reverse=True)
            for line in lines:
                x1, y1, x2, y2 = line[0]
                if (y1 < center_y and y2 > center_y) or (y1 > center_y and y2 < center_y):
                    angle_rad = math.atan2(y2 - y1, x2 - x1)
                    angle_deg = math.degrees(angle_rad)
                    
                    # Determine direction based on angle
                    if (-90 <= angle_deg <= -45) or (45 <= angle_deg <= 90):
                        direction = 'forward'
                    elif (0 <= angle_deg < 45):
                        direction = 'ccw'
                    elif (-45 <= angle_deg < 0):
                        direction = 'cw'
                    else:
                        direction = 'stop'
                    break
        
        # Publish command to wheel command node
        self.publisher_.publish(String(data=direction))


def main(args=None):
    rclpy.init(args=args)

    # Start camera processor node
    camera_processor = CameraProcessorNode()

    rclpy.spin(camera_processor)

    # Shutdown on exit
    camera_processor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
