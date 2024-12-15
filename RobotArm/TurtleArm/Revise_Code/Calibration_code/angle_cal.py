import numpy as np
import math

# 두 직선의 점 좌표
point1_line1 = np.array([0.74302, 0.35215])
point2_line1 = np.array([0, 0])
point1_line2 = np.array([0.47537, -0.16519])
point2_line2 = np.array([0, 0])

# 벡터 계산
vector1 = point1_line1 - point2_line1
vector2 = point1_line2 - point2_line2

# 벡터의 내적과 크기 계산
dot_product = np.dot(vector1, vector2)
magnitude1 = np.linalg.norm(vector1)
magnitude2 = np.linalg.norm(vector2)

# 두 벡터 사이의 각도 계산 (라디안 단위)
cos_theta = dot_product / (magnitude1 * magnitude2)
angle_radians = np.arccos(np.clip(cos_theta, -1.0, 1.0))

# 라디안을 각도로 변환
angle_degrees = math.degrees(angle_radians)
print("두 직선 사이의 각도:", angle_degrees, "도")
