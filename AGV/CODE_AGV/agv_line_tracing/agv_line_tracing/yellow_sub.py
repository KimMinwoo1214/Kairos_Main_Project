import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

class AGVControlSubscriber(Node):
    def __init__(self):
        super().__init__('agv_control_subscriber')
        self.subscription = self.create_subscription(String, 'agv_direction', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning
        self.port = serial.Serial(port="/dev/ttyAMA2", baudrate=115200, timeout=0.1)
        time.sleep(2)  # Wait for the serial port to initialize

    def listener_callback(self, msg):
        direction = msg.data
        self.get_logger().info(f'Received direction: {direction}')

        if direction == "forward":
            self.send_wheel_command(133, 128, 128)  # Adjusted for forward
        elif direction == "cw":
            self.send_wheel_command(128, 128, 126)  # Adjusted for clockwise
        elif direction == "ccw":
            self.send_wheel_command(128, 128, 130)  # Adjusted for counterclockwise
        else:
            self.send_wheel_command(128, 128, 128)  # Stop

    def send_wheel_command(self, direction_1, direction_2, direction_3):
        HEADER = 0xFE
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

    def destroy_node(self):
        super().destroy_node()
        if self.port.is_open:
            self.port.close()
        self.get_logger().info("Serial port closed.")

def main(args=None):
    rclpy.init(args=args)
    agv_control_subscriber = AGVControlSubscriber()
    rclpy.spin(agv_control_subscriber)
    agv_control_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

