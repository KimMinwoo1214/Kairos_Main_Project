import cv2
import numpy as np

# Camera intrinsic parameters
camera_matrix = np.array([[638.71849854, 0, 346.51236862],
                          [0, 635.92738363, 237.44836475],
                          [0, 0, 1]])
dist_coeffs = np.array([0.25570537, -1.18457981, -0.00670271, 0.01808242, 1.49729085])

# 3D LiDAR points (in the LiDAR coordinate system)
lidar_points = np.array([[0.74381, -0.24219, 0],
                         [0.65859, -0.17031, 0],
                         [0.73813, 0.12416, 0],
                         [0.66587, 0.12898, 0],
                         [0.66386, 0.25296, 0]], dtype=np.float32)

# Corresponding 2D camera points (in the image coordinate system)
image_points = np.array([[601, 149],
                         [566, 149],
                         [351, 149],
                         [232, 149],
                         [216, 149]], dtype=np.float32)

# Solve PnP to get rotation and translation vectors
success, rotation_vector, translation_vector = cv2.solvePnP(lidar_points, image_points, camera_matrix, dist_coeffs)

if success:
    # Convert rotation vector to rotation matrix
    rotation_matrix, _ = cv2.Rodrigues(rotation_vector)

    print("Rotation Matrix:")
    print(rotation_matrix)
    print("\nTranslation Vector:")
    print(translation_vector)
else:
    print("PnP solution failed.")
