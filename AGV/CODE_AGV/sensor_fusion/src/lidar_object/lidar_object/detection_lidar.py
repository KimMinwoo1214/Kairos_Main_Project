import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from math import cos, sin

class ObstacleDetector(Node):
    def __init__(self):
        super().__init__('obstacle_detector')
        
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            depth=10
        )
        
        self.scan_subscriber = self.create_subscription(
            LaserScan, '/scan', self.scan_callback, qos_profile)
        self.obstacle_publisher = self.create_publisher(
            Bool, '/obstacle_detected', qos_profile)
        self.marker_publisher = self.create_publisher(
            Marker, '/obstacle_marker', qos_profile)

        self.obstacle_threshold = 1.5
        self.get_logger().info("ObstacleDetector node started with QoS: BestEffort")

    def scan_callback(self, msg):
        self.get_logger().info(f"Received LaserScan data with {len(msg.ranges)} ranges")
        self.get_logger().info(f"First few ranges: {msg.ranges[:5]}")

        obstacle_detected = False
        marker = Marker()
        marker.header.frame_id = "base_link"
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = "obstacles"
        marker.id = 0
        marker.type = Marker.SPHERE_LIST
        marker.action = Marker.ADD
        marker.pose.orientation.w = 1.0
        marker.scale.x = 0.5
        marker.scale.y = 0.5
        marker.scale.z = 0.5
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0

        for angle, distance in enumerate(msg.ranges):
            if 0.0 < distance < self.obstacle_threshold:
                obstacle_detected = True
                angle_rad = msg.angle_min + angle * msg.angle_increment
                x = distance * cos(angle_rad)
                y = distance * sin(angle_rad)
                point = Point()
                point.x = x
                point.y = y
                point.z = 0.0
                marker.points.append(point)
                self.get_logger().info(f"Obstacle detected at x: {x:.2f}, y: {y:.2f}")

        if marker.points:
            self.get_logger().info(f"Publishing marker with {len(marker.points)} points to /obstacle_marker")
            self.marker_publisher.publish(marker)
        else:
            self.get_logger().warn("No points in marker to publish - check obstacle_threshold and sensor data.")

        self.obstacle_publisher.publish(Bool(data=obstacle_detected))

def main(args=None):
    rclpy.init(args=args)
    obstacle_detector = ObstacleDetector()
    rclpy.spin(obstacle_detector)
    obstacle_detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
