import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math

class LiDARFilterNode(Node):
    def __init__(self):
        super().__init__('lidar_filter_node')
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',  # LiDAR 데이터가 퍼블리시되는 토픽 이름을 확인하고 맞춰주세요
            self.lidar_callback,
            10
        )

    def lidar_callback(self, msg):
        count = int(msg.scan_time / msg.time_increment)
        self.get_logger().info(f"I heard a laser scan {msg.header.frame_id}[{count}]:")
        self.get_logger().info(f"angle_range : [{math.degrees(msg.angle_min)}, {math.degrees(msg.angle_max)}]")

        for i in range(count):
            degree = math.degrees(msg.angle_min + msg.angle_increment * i)
            # 특정 각도 범위 (-21.5도에서 21.5도)에서만 출력
            if -21.5 <= degree <= 21.5:
                self.get_logger().info(f"angle-distance : [{degree}, {msg.ranges[i]}]")

def main(args=None):
    rclpy.init(args=args)
    lidar_filter_node = LiDARFilterNode()
    rclpy.spin(lidar_filter_node)
    lidar_filter_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
