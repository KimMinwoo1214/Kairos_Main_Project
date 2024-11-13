import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy  # QoS 설정을 위한 임포트
from sensor_msgs.msg import PointCloud2, Image
from cv_bridge import CvBridge
import tf2_ros
import numpy as np
import cv2

class PointCloudToImageProjector(Node):
    def __init__(self):
        super().__init__('pointcloud_to_image_projector')

        # Best Effort QoS 설정
        qos_profile = QoSProfile(reliability=QoSReliabilityPolicy.BEST_EFFORT)

        # 구독 및 퍼블리셔 생성
        self.subscription = self.create_subscription(
            PointCloud2,
            '/pointcloud',  # 실제 토픽 이름과 일치하는지 확인
            self.pointcloud_callback,
            qos_profile)
        self.image_publisher = self.create_publisher(Image, '/projected_image', qos_profile)
        
        self.bridge = CvBridge()
        
        # 카메라 내부 파라미터
        self.camera_matrix = np.array([[638.71849854, 0, 346.51236862],
                                       [0, 635.92738363, 237.44836475],
                                       [0, 0, 1]])
        self.dist_coeffs = np.array([0.25570537, -1.18457981, -0.00670271, 0.01808242, 1.49729085])
        
        # 카메라와 라이다 사이의 외부 파라미터
        self.rotation_matrix = np.array([[-0.50941863, -0.83896701, -0.19138188],
                                         [0.24829726, 0.06963523, -0.96617773],
                                         [0.82391816, -0.53970853, 0.17283973]])
        self.translation_vector = np.array([[0.32358104], [-0.17807832], [-0.03323078]])
        
        # tf2 버퍼와 리스너 초기화
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)

    def pointcloud_callback(self, msg):
        points = self.pointcloud2_to_xyz(msg)
        
        # 라이다의 좌표를 카메라 좌표계로 변환
        points_cam = self.transform_to_camera_frame(points)
        
        # 변환된 포인트를 카메라 이미지로 투영
        image = self.project_points_to_image(points_cam)
        
        # 이미지 퍼블리시
        self.image_publisher.publish(self.bridge.cv2_to_imgmsg(image, encoding="bgr8"))
        self.get_logger().info("Published projected image to /projected_image")

    def pointcloud2_to_xyz(self, pointcloud_msg):
        cloud_data = np.frombuffer(pointcloud_msg.data, dtype=np.float32).reshape(-1, 4)
        return cloud_data[:, :3]  # XYZ 데이터만 추출

    def transform_to_camera_frame(self, points):
        # 포인트 클라우드를 카메라 좌표계로 변환
        points_h = np.hstack((points, np.ones((points.shape[0], 1))))  # 동차 좌표로 확장
        # 회전 및 이동 행렬 적용
        points_cam = (self.rotation_matrix @ points.T + self.translation_vector).T
        return points_cam  # 변환된 좌표 반환

    def project_points_to_image(self, points_cam):
        # 왜곡 보정을 포함하여 3D 포인트를 2D 이미지 좌표로 투영
        image = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # 카메라 좌표에서 유효한 포인트만 선택
        valid_points = points_cam[points_cam[:, 2] > 0]
        
        # 투영하여 이미지 좌표로 변환
        projected_points, _ = cv2.projectPoints(
            valid_points, 
            np.zeros(3), np.zeros(3),  # 회전 및 이동은 이미 변환되었으므로 0으로 설정
            self.camera_matrix, 
            self.dist_coeffs
        )
        
        # 이미지 상의 좌표에 점 표시
        for point in projected_points:
            u, v = int(point[0][0]), int(point[0][1])
            if 0 <= u < image.shape[1] and 0 <= v < image.shape[0]:
                image[v, u] = (255, 255, 255)  # 흰색으로 점 그리기
        
        return image

def main(args=None):
    rclpy.init(args=args)
    projector = PointCloudToImageProjector()
    rclpy.spin(projector)
    projector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
