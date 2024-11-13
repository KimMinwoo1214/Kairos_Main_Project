#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy
from sensor_msgs.msg import PointCloud2, Image
from cv_bridge import CvBridge
import tf2_ros
import numpy as np
import cv2

class PointCloudToImageProjector(Node):
    def __init__(self):
        super().__init__('pointcloud_to_image_projector')

        # QoS 설정: Best Effort, Keep Last 10
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10
        )

        # 구독 및 퍼블리셔 설정
        self.pointcloud_subscription = self.create_subscription(
            PointCloud2,
            '/point_cloud',  # 라이다 데이터 토픽
            self.pointcloud_callback,
            qos_profile
        )
        self.image_subscription = self.create_subscription(
            Image,
            '/camera_image',  # 카메라 이미지 토픽
            self.image_callback,
            qos_profile
        )
        self.image_publisher = self.create_publisher(Image, '/projected_image', qos_profile)
        
        self.bridge = CvBridge()
        self.last_image = None  # 마지막 카메라 이미지를 저장하기 위한 변수

        # 카메라 내부 파라미터 설정
        self.camera_matrix = np.array([[638.71849854, 0, 346.51236862],
                                       [0, 635.92738363, 237.44836475],
                                       [0, 0, 1]])
        self.dist_coeffs = np.array([0.25570537, -1.18457981, -0.00670271, 0.01808242, 1.49729085])
        
        # 카메라와 라이다 사이의 외부 파라미터 설정
        self.rotation_matrix = np.array([[0.98776919, -0.15192251, -0.03509381],
                                         [-0.0564974, -0.13894991, -0.98868648],
                                         [0.14532745, 0.97857676, -0.14583367]])
        self.translation_vector = np.array([[-0.6979478], [0.01893904], [0.05232775]])
        
        # tf2 버퍼와 리스너 초기화
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

    def image_callback(self, msg):
        # 카메라 이미지 저장
        self.last_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

    def pointcloud_callback(self, msg):
        if self.last_image is None:
            # 이미지가 아직 수신되지 않았다면 포인트 클라우드 처리 생략
            return

        # 포인트 클라우드를 XYZ 배열로 변환
        points = self.pointcloud2_to_xyz(msg)
        
        # 라이다 좌표계를 카메라 좌표계로 변환
        points_cam = self.transform_to_camera_frame(points)
        
        # 기존 이미지 위에 포인트를 투영
        projected_image = self.project_points_to_image(points_cam, self.last_image.copy())
        
        # 결과 이미지 퍼블리시
        self.image_publisher.publish(self.bridge.cv2_to_imgmsg(projected_image, encoding="bgr8"))
        self.get_logger().info("Published projected image to /projected_image")

    def pointcloud2_to_xyz(self, pointcloud_msg):
        # PointCloud2 데이터를 XYZ 포인트 배열로 변환
        cloud_data = np.frombuffer(pointcloud_msg.data, dtype=np.float32).reshape(-1, 4)
        return cloud_data[:, :3]  # XYZ 데이터만 추출

    def transform_to_camera_frame(self, points):
        # 포인트 클라우드를 카메라 좌표계로 변환
        points_h = np.hstack((points, np.ones((points.shape[0], 1))))  # 동차 좌표로 확장
        # 회전 및 이동 행렬 적용
        points_cam = (self.rotation_matrix @ points.T + self.translation_vector).T
        return points_cam  # 변환된 좌표 반환

    def project_points_to_image(self, points_cam, image):
        # 왜곡 보정을 포함하여 3D 포인트를 2D 이미지 좌표로 투영
        valid_points = points_cam[points_cam[:, 2] > 0]  # 유효한 Z 좌표 필터링
        
        # 투영하여 이미지 좌표로 변환
        projected_points, _ = cv2.projectPoints(
            valid_points, 
            np.zeros(3), np.zeros(3),  # 회전 및 이동은 이미 변환되었으므로 0으로 설정
            self.camera_matrix, 
            self.dist_coeffs
        )
        
        # 기존 이미지 위에 투영된 포인트 그리기
        for point in projected_points:
            u, v = int(point[0][0]), int(point[0][1])
            if 0 <= u < image.shape[1] and 0 <= v < image.shape[0]:
                cv2.circle(image, (u, v), 3, (0, 255, 0), -1)  # 녹색 점으로 표시
        
        return image

def main(args=None):
    rclpy.init(args=args)
    projector = PointCloudToImageProjector()
    rclpy.spin(projector)
    projector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
