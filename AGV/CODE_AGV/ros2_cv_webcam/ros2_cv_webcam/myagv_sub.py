import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time
import threading

HEADER = 0xFE

class WheelCommandNode(Node):
    def __init__(self):
        super().__init__('wheel_command_node')
        # Subscriber to receive commands from camera processor node
        self.subscription = self.create_subscription(String, 'wheel_command', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

        # Initialize serial port
        try:
            self.port = serial.Serial(port="/dev/ttyAMA2", baudrate=115200, timeout=0.1)
            time.sleep(2)
        except serial.SerialException as e:
            self.get_logger().error(f'Failed to open serial port: {e}')
            self.port = None

        # Start a thread to send wheel commands
        self.direction_1, self.direction_2, self.direction_3 = 128, 128, 128
        self.rotation_sequence = None
        self.sequence_state = None
        self.sequence_start_time = 0
        self.move_thread = threading.Thread(target=self.move_robot, daemon=True)
        self.move_thread.start()

    def listener_callback(self, msg):
        current_time = time.time()
        command = msg.data

        # Handle rotation sequences if in progress
        if self.rotation_sequence is not None:
            if self.sequence_state == "forward":
                if current_time - self.sequence_start_time >= 1.5:
                    # Transition to rotating state
                    self.sequence_state = "rotating"
                    self.sequence_start_time = current_time
                    if self.rotation_sequence == "cw":
                        # Set directions for clockwise rotation
                        self.direction_1, self.direction_2, self.direction_3 = 128, 128, 126  # Adjust as needed for rotation
                        self.get_logger().info("Starting clockwise rotation.")
                    elif self.rotation_sequence == "ccw":
                        # Set directions for counterclockwise rotation
                        self.direction_1, self.direction_2, self.direction_3 = 128, 128, 130  # Adjust as needed for rotation
                        self.get_logger().info("Starting counterclockwise rotation.")
            elif self.sequence_state == "rotating":
                if current_time - self.sequence_start_time >= 3.0:
                    # Rotation completed, stop
                    self.direction_1, self.direction_2, self.direction_3 = 128, 128, 128  # Stop
                    self.get_logger().info(f"{self.rotation_sequence.upper()} rotation completed. Stopping.")
                    self.rotation_sequence = None
                    self.sequence_state = None
            # During rotation sequence, skip processing new commands
            return

        # Only process new commands if not in a rotation sequence
        if command == 'forward':
            self.direction_1, self.direction_2, self.direction_3 = 133, 128, 128  # Move forward
        elif command == 'cw':
            # Start clockwise rotation sequence
            self.rotation_sequence = "cw"
            self.sequence_state = "forward"
            self.sequence_start_time = current_time
            self.direction_1, self.direction_2, self.direction_3 = 133, 128, 128  # Move forward for 1.5 seconds before rotating
            self.get_logger().info("Initiating clockwise rotation sequence: Moving forward first.")
        elif command == 'ccw':
            # Start counterclockwise rotation sequence
            self.rotation_sequence = "ccw"
            self.sequence_state = "forward"
            self.sequence_start_time = current_time
            self.direction_1, self.direction_2, self.direction_3 = 133, 128, 128  # Move forward for 1.5 seconds before rotating
            self.get_logger().info("Initiating counterclockwise rotation sequence: Moving forward first.")
        elif command == 'stop':
            self.direction_1, self.direction_2, self.direction_3 = 128, 128, 128  # Stop

    def move_robot(self):
        while True:
            if self.port:
                command = [
                    HEADER,
                    HEADER,
                    self.direction_1,
                    self.direction_2,
                    self.direction_3,
                    (self.direction_1 + self.direction_2 + self.direction_3) & 0xFF  # Checksum
                ]
                try:
                    self.port.write(bytearray(command))
                    self.port.flush()
                except serial.SerialException as e:
                    self.get_logger().error(f'Serial communication error: {e}')
            time.sleep(0.1)  # Send command every 100ms

        # On exit, send stop command
        if self.port:
            self.port.write(bytearray([HEADER, HEADER, 128, 128, 128, (128 + 128 + 128) & 0xFF]))
            self.port.close()
            self.get_logger().info('Serial port closed. Program terminated.')


def main(args=None):
    import rclpy
    rclpy.init(args=args)

    # Start wheel command node
    wheel_command = WheelCommandNode()

    rclpy.spin(wheel_command)

    # Shutdown on exit
    wheel_command.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
