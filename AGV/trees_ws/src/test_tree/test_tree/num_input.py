import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class ManualNumberInput(Node):
    """
    키보드 입력을 통해 숫자를 퍼블리시하는 노드.
    """
    def __init__(self):
        super().__init__('manual_number_input')
        self.publisher = self.create_publisher(Int32, '/input_number', 10)
        self.get_logger().info("Listening for keyboard input to publish numbers to /input_number")

    def publish_number(self):
        """
        키보드로 입력받은 숫자를 퍼블리시.
        """
        while rclpy.ok():
            try:
                # 숫자 입력
                number = int(input("Enter a number to publish to /input_number: "))
                self.publisher.publish(Int32(data=number))
                self.get_logger().info(f"Published number: {number}")
            except ValueError:
                # 유효하지 않은 입력 처리
                self.get_logger().warn("Invalid input. Please enter a valid integer.")
            except KeyboardInterrupt:
                # Ctrl+C로 종료
                self.get_logger().info("Shutting down manual number input.")
                break


def main(args=None):
    rclpy.init(args=args)
    node = ManualNumberInput()
    try:
        # 숫자 입력 대기 및 퍼블리시
        node.publish_number()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
