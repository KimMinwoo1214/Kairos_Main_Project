#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import serial
import time

# Global variables for wheel directions and state
direction_1, direction_2, direction_3 = 128, 128, 128  # Default stop
rotation_sequence = None  # None, 'cw', 'ccw'
sequence_state = None     # 'forward', 'rotating'
sequence_start_time = 0
HEADER = 0xFE
obstacle_detected = False  # 장애물 감지 플래그

def send_wheel_command(port, direction_1, direction_2, direction_3):
    """
    Send wheel command to the AGV via serial port.
    """
    command = [
        HEADER,
        HEADER,
        direction_1,
        direction_2,
        direction_3,
        (direction_1 + direction_2 + direction_3) & 0xFF  # Checksum
    ]
    try:
        port.write(bytearray(command))
        port.flush()
    except serial.SerialException as e:
        rospy.logerr(f"Serial communication error: {e}")

def direction_callback(data):
    """
    Callback function to handle received direction commands.
    """
    global direction_1, direction_2, direction_3, rotation_sequence, sequence_state, sequence_start_time
    global obstacle_detected

    direction = data.data
    rospy.loginfo(f"Received direction: {direction}")

    # 장애물이 감지되었으면 모든 모터를 정지
    if obstacle_detected:
        direction_1, direction_2, direction_3 = 128, 128, 128  # Stop command
        rospy.logwarn("Obstacle detected! Stopping AGV.")
        send_wheel_command(port, direction_1, direction_2, direction_3)
        return  # 바로 리턴하여 정지 유지

    # Update wheel commands based on direction
    current_time = time.time()

    if direction == "f":
        direction_1, direction_2, direction_3 = 128 + 5, 128, 128  # Move forward
    elif direction == "cw":
        rotation_sequence = "cw"
        sequence_state = "forward"
        sequence_start_time = current_time
        direction_1, direction_2, direction_3 = 128 + 5, 128, 128  # Move forward
        rospy.loginfo("Initiating clockwise rotation sequence: Moving forward.")
    elif direction == "ccw":
        rotation_sequence = "ccw"
        sequence_state = "forward"
        sequence_start_time = current_time
        direction_1, direction_2, direction_3 = 128 + 5, 128, 128  # Move forward
        rospy.loginfo("Initiating counterclockwise rotation sequence: Moving forward.")
    else:
        direction_1, direction_2, direction_3 = 128, 128, 128  # Unknown, stop

    send_wheel_command(port, direction_1, direction_2, direction_3)

def obstacle_detect_callback(data):
    """
    Callback function for obstacle detection.
    """
    global obstacle_detected
    obstacle_detected = data.data == "true"
    rospy.loginfo(f"Obstacle detection updated: {obstacle_detected}")

def main():
    global port

    rospy.init_node('wheel_controller')

    # Initialize serial port (adjust the port name as needed)
    port = serial.Serial(port="/dev/ttyAMA2", baudrate=115200, timeout=0.1)
    time.sleep(2)  # Wait for the serial port to initialize

    rospy.Subscriber('direction_commands', String, direction_callback)
    rospy.Subscriber('obstacle_detected', String, obstacle_detect_callback)

    # Spin to keep the node running
    rospy.spin()

    # On exit, send stop command
    send_wheel_command(port, 128, 128, 128)
    time.sleep(0.1)  # Ensure the stop command is sent

    # Close the serial port
    if port.is_open:
        port.close()
    rospy.loginfo("Serial port closed. Program terminated.")

if __name__ == "__main__":
    main()
