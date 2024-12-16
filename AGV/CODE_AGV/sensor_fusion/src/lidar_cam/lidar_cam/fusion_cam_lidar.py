import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, LaserScan
from cv_bridge import CvBridge
import numpy as np
import cv2
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

class LidarCameraFusion(Node):
    def __init__(self):
        super().__init__('lidar_camera_fusion')

        # QoS 프로파일 설정: BEST_EFFORT 사용
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10
        )

        # 카메라와 LiDAR 구독에 QoS 프로파일 적용
        self.camera_sub = self.create_subscription(Image, '/video_frames', self.camera_callback, qos_profile)
        self.lidar_sub = self.create_subscription(LaserScan, '/scan', self.lidar_callback, qos_profile)
        self.bridge = CvBridge()
        self.lidar_points = []

        # Camera intrinsics
        self.camera_matrix = np.array([[638.71849854, 0, 346.51236862],
                                       [0, 635.92738363, 237.44836475],
                                       [0, 0, 1]])
        self.dist_coeffs = np.array([0.25570537, -1.18457981, -0.00670271, 0.01808242, 1.49729085])

        # Extrinsics (Rotation and Translation)
        self.rotation_matrix = np.array([[-0.50941863, -0.83896701, -0.19138188],
                                         [0.24829726, 0.06963523, -0.96617773],
                                         [0.82391816, -0.53970853, 0.17283973]])
        self.translation_vector = np.array([[0.32358104], [-0.17807832], [-0.03323078]])

    def lidar_callback(self, msg):
        self.get_logger().info("Received LiDAR data")
        self.lidar_points = []
        angle = -0.3752458  # -21.5 degrees in radians
        for r in msg.ranges:
            if msg.range_min < r < msg.range_max and -0.3752458 <= angle <= 0.42760566:  # Filter angle between -21.5 and 24.5 degrees
                # Convert polar coordinates to Cartesian (x, y)
                x = r * np.cos(angle)
                y = r * np.sin(angle)
                # Assume LiDAR is at z = 0
                self.lidar_points.append([x, y, 0.0])
            angle += msg.angle_increment

    def camera_callback(self, msg):
        self.get_logger().info("Received Camera frame")
        # Convert ROS Image message to OpenCV image
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg)  # Use default encoding
        except Exception as e:
            self.get_logger().error(f"Failed to convert image: {e}")
            return

        if not self.lidar_points:
            self.get_logger().info("No LiDAR points to project")
            cv2.imshow('LiDAR-Camera Fusion', cv_image)
            cv2.waitKey(1)
            return

        # Manually project LiDAR data onto specific x-range of the image
        img_height, img_width = cv_image.shape[:2]
        angle_range = 0.42760566 + 0.3752458  # Total angle range in radians (24.5 + 21.5 degrees)

        for point in self.lidar_points:
            x, y, _ = point
            # Use y value to find angle and map it to image x-coordinate
            if y != 0:  # Avoid division by zero
                angle = np.arctan2(y, x)
                x_img = int(((angle + 0.3752458) / angle_range) * img_width)

                y_img = 108  # Fixed y value in the image

                # Draw projected point within image bounds
                if 0 <= x_img < img_width:
                    cv2.circle(cv_image, (x_img, y_img), 3, (0, 255, 0), -1)

        # Display the image
        cv2.imshow('LiDAR-Camera Fusion', cv_image)
        cv2.waitKey(1)

def main():
    rclpy.init()  # ROS 통신 시작
    node = LidarCameraFusion()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

