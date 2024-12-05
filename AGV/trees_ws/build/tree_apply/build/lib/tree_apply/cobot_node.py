import rclpy
from rclpy.node import Node
from pymycobot.mycobot import MyCobot
from std_msgs.msg import String, Bool

class CobotNode(Node):
    def __init__(self):
        super().__init__('cobot_node')

        # MyCobot 제어 객체 초기화
        self.cobot = MyCobot('/dev/ttyACM0', 115200)

        # 명령 처리
        self.subscription = self.create_subscription(
            String,
            'cobot_move_command',
            self.move_cobot,
            10
        )

        # 상태 피드백 퍼블리셔
        self.feedback_publisher = self.create_publisher(Bool, 'cobot_move_feedback', 10)

        self.get_logger().info("Cobot Node initialized and waiting for commands...")

    def move_cobot(self, msg):
        try:
            # 명령 수신
            angles = list(map(float, msg.data.split(',')))  # 메시지를 각도로 변환
            self.get_logger().info(f"Moving Cobot to angles: {angles}")

            # 각 조인트 각도 설정
            for i, angle in enumerate(angles):
                self.cobot.send_angle(i + 1, angle, 20)
                self.get_logger().info(f"Joint {i + 1} moved to {angle}")
                self.cobot.wait(0.5)

            # 완료 피드백 발행
            self.feedback_publisher.publish(Bool(data=True))
            self.get_logger().info("Cobot movement completed and feedback sent.")

        except Exception as e:
            self.get_logger().error(f"Failed to execute move command: {str(e)}")
            self.feedback_publisher.publish(Bool(data=False))  # 실패 피드백 발행


def main(args=None):
    rclpy.init(args=args)
    node = CobotNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
