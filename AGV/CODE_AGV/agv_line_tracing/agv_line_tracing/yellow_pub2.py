#!/usr/bin/env python

import cv2
import numpy as np
import math
import rospy
from std_msgs.msg import String

def calculate_yellow_line_angle_live(pub):
    """
    Capture video from the camera, detect yellow lines, and publish direction commands.
    """
    # Start camera capture (0 is the default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        rospy.logerr("Cannot open camera.")
        return

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            rospy.logerr("Cannot receive frame.")
            break

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
                    direction  = "Unknown"

                # Publish the detected direction
                pub.publish(direction)
                rospy.loginfo(f"Published direction: {direction}")
                break  # Only process the first relevant line

        # Display the output frame (optional)
        cv2.imshow('Yellow Line Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

def main():
    rospy.init_node('yellow_line_detector')
    pub = rospy.Publisher('direction_commands', String, queue_size=10)

    # Start lane detection and command update
    calculate_yellow_line_angle_live(pub)

if __name__ == "__main__":
    main()

# launch file (line_tracing_launch.py)
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='agv_line_tracing',
            executable='yellow_pub2',
            name='yellow_pub2',
            output='screen'
        ),
        Node(
            package='agv_line_tracing',
            executable='yellow_sub2',
            name='yellow_sub2',
            output='screen'
        ),
    ])

