#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

HEADER = 0xFE
obstacle_detected = False  # 장애물 감지 플래그

class WheelController(Node):
    def __init__(self):
        super().__init__('wheel_controller')
        self.port = serial.Serial(port="/dev/ttyAMA2", baudrate=115200, timeout=0.1)
        time.sleep(2)  # Wait for the serial port to initialize

        self.direction_1, self.direction_2, self.direction_3 = 128, 128, 128  # Default stop
        self.create_subscription(String, 'direction_commands', self.direction_callback, 10)
        self.create_subscription(String, 'obstacle_detected', self.obstacle_detect_callback, 10)

    def send_wheel_command(self, direction_1, direction_2, direction_3):
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
            self.port.write(bytearray(command))
            self.port.flush()
        except serial.SerialException as e:
            self.get_logger().error(f"Serial communication error: {e}")

    def direction_callback(self, msg):
        """
        Callback function to handle received direction commands.
        """
        global obstacle_detected
        direction = msg.data
        self.get_logger().info(f"Received direction: {direction}")

        # 장애물이 감지되었으면 모든 모터를 정지
        if obstacle_detected:
            self.direction_1, self.direction_2, self.direction_3 = 128, 128, 128  # Stop command
            self.get_logger().warn("Obstacle detected! Stopping AGV.")
            self.send_wheel_command(self.direction_1, self.direction_2, self.direction_3)
            return  # 바로 리턴하여 정지 유지

        # Update wheel commands based on direction
        if direction == "f":
            self.direction_1, self.direction_2, self.direction_3 = 128 + 5, 128, 128  # Move forward
        elif direction == "cw":
            self.direction_1, self.direction_2, self.direction_3 = 128, 128 + 5, 128  # Rotate clockwise
        elif direction == "ccw":
            self.direction_1, self.direction_2, self.direction_3 = 128, 128, 128 + 5  # Rotate counterclockwise
        else:
            self.direction_1, self.direction_2, self.direction_3 = 128, 128, 128  # Unknown, stop

        self.send_wheel_command(self.direction_1, self.direction_2, self.direction_3)

    def obstacle_detect_callback(self, msg):
        """
        Callback function for obstacle detection.
        """
        global obstacle_detected
        obstacle_detected = msg.data == "true"
        self.get_logger().info(f"Obstacle detection updated: {obstacle_detected}")

    def destroy_node(self):
        super().destroy_node()
        # Send stop command and close the serial port on exit
        self.send_wheel_command(128, 128, 128)
        time.sleep(0.1)
        if self.port.is_open:
            self.port.close()
        self.get_logger().info("Serial port closed. Program terminated.")

def main(args=None):
    rclpy.init(args=args)
    wheel_controller = WheelController()
    rclpy.spin(wheel_controller)
    wheel_controller.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
