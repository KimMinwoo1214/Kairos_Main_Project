#!/usr/bin/env python

import cv2
import numpy as np
import math
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class YellowLineDetector(Node):
    def __init__(self):
        super().__init__('yellow_line_detector')
        self.pub = self.create_publisher(String, 'direction_commands', 10)
        self.timer = self.create_timer(0.1, self.calculate_yellow_line_angle_live)

        # Start camera capture (0 is the default camera)
        self.cap = cv2.VideoCapture(1)
        if not self.cap.isOpened():
            self.get_logger().error("Cannot open camera.")

    def calculate_yellow_line_angle_live(self):
        """
        Capture video from the camera, detect yellow lines, and publish direction commands.
        """
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().error("Cannot receive frame.")
            return

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define yellow color range in HSV
        lower_yellow = np.array([15, 100, 100])
        upper_yellow = np.array([35, 255, 255])

        # Create yellow mask
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # Edge detection and Hough Transform to detect lines
        edges = cv2.Canny(mask, 50, 200)
        lines = cv2.HoughLinesP(edges, 1, math.pi / 180, threshold=30, minLineLength=30, maxLineGap=10)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                angle_rad = math.atan2(y2 - y1, x2 - x1)
                angle_deg = math.degrees(angle_rad)

                # Determine direction based on angle
                if (-90 <= angle_deg <= -45) or (45 <= angle_deg <= 90):
                    direction = "f"  # Forward
                elif (0 <= angle_deg < 45):
                    direction = "ccw"  # Clockwise
                elif (-45 <= angle_deg < 0):
                    direction = "cw"  # Counterclockwise
                else:
                    direction = "Unknown"

                # Publish the detected direction
                self.pub.publish(String(data=direction))
                self.get_logger().info(f"Published direction: {direction}")
                break  # Only process the first relevant line

        # Display the output frame (optional)
        cv2.imshow('Yellow Line Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            rclpy.shutdown()

    def destroy_node(self):
        super().destroy_node()
        self.cap.release()
        cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    yellow_line_detector = YellowLineDetector()
    rclpy.spin(yellow_line_detector)
    yellow_line_detector.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
