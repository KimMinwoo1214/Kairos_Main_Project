#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys
import select
import termios
import tty

# Key mapping
move_bindings = {
    'w': 'forward',
    'a': 'ccw',
    'd': 'cw',
    's': 'stop',
}

def get_key(settings):
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

class TeleopController(Node):
    def __init__(self):
        super().__init__('teleop_controller')
        self.pub = self.create_publisher(String, 'teleop_commands', 10)
        self.get_logger().info("Control the AGV with w (forward), a (ccw), d (cw), s (stop)")
        self.get_logger().info("Press Ctrl+C to quit")

def main():
    rclpy.init()
    node = TeleopController()

    # 터미널 설정을 위한 환경 변수
    settings = termios.tcgetattr(sys.stdin)

    try:
        while rclpy.ok():
            key = get_key(settings)
            if key in move_bindings:
                command = move_bindings[key]
                msg = String()
                msg.data = command
                node.pub.publish(msg)
                node.get_logger().info(f"Published command: {command}")
            elif key == '\x03':  # Ctrl+C
                break

    except Exception as e:
        node.get_logger().error(f"Error: {e}")

    finally:
        # 종료 시 정지 명령 전송
        msg = String()
        msg.data = "stop"
        node.pub.publish(msg)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        rclpy.shutdown()

if __name__ == "__main__":
    main()
