#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StopConditionEvaluator(Node):
    def __init__(self):
        super().__init__('stop_condition_evaluator')
        self.obstacle_detected = False
        self.video_signal_detected = False  # video_signal의 감지 상태

        # Subscribers
        self.obstacle_subscription = self.create_subscription(
            String, 'obstacle_detected', self.obstacle_callback, 10
        )
        self.video_signal_subscription = self.create_subscription(
            String, 'detection_status', self.video_signal_callback, 10
        )

        # Publisher
        self.stop_publisher = self.create_publisher(String, 'stop_signal', 10)

    def obstacle_callback(self, data):
        # 장애물 감지 상태 업데이트
        self.obstacle_detected = data.data == "true"
        self.evaluate_conditions()

    def video_signal_callback(self, data):
        # 영상 감지 상태 업데이트
        self.video_signal_detected = data.data == "true"
        self.evaluate_conditions()

    def evaluate_conditions(self):
        # 두 조건이 모두 만족될 때만 stop 신호 퍼블리시
        if self.obstacle_detected and self.video_signal_detected:
            self.get_logger().info("Both conditions met. Publishing stop signal.")
            self.stop_publisher.publish(String(data="stop"))
        else:
            self.get_logger().info("Conditions not met. No stop signal sent.")

def main(args=None):
    rclpy.init(args=args)
    node = StopConditionEvaluator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
