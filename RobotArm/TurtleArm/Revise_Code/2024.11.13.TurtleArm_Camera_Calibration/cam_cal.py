import numpy as np
import cv2
import glob
import os

# 디버깅: 현재 디렉토리 확인
print("Current directory:", os.getcwd())
print("Files in the current directory:")
print(os.listdir('/home/pi/Revise_Code/2024.11.13.TurtleArm_Camera_Calibration'))  # List all files in the current directory

# 체커보드 크기와 각 사각형의 크기
checkerboard_size = (11, 7)  # Define the size of the checkerboard (internal corners)
square_size = 23  # mm, size of each square in the checkerboard

# 종료 기준 설정 (criteria for subpixel corner refinement)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# 체커보드의 3D 점 준비 (prepare 3D object points)
objp = np.zeros((checkerboard_size[0] * checkerboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:checkerboard_size[0], 0:checkerboard_size[1]].T.reshape(-1, 2)
objp *= square_size  # Scale by square size to represent real-world units (mm)

# 객체 포인트와 이미지 포인트를 저장할 배열
objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane

# 체커보드 이미지 파일 불러오기 (load checkerboard images)
images = glob.glob('/home/pi/Revise_Code/2024.11.13.TurtleArm_Camera_Calibration/*.jpg')  # Adjust this path if needed for your image files
print(f"Found {len(images)} images.")  # Debug: Check how many images were found

# No images found
if len(images) == 0:
    print("Error: No images found. Please check the directory and file pattern.")
    exit()

gray = None

# 체커보드 코너 찾기 및 이미지 처리 (Find checkerboard corners in each image)
for fname in images:
    img = cv2.imread(fname)
    if img is None:
        print(f"Error: Could not load image {fname}")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 체커보드 코너 찾기 (find chessboard corners)
    ret, corners = cv2.findChessboardCorners(gray, checkerboard_size, None)

    # 디버깅 메시지 추가 (debugging message for corner detection)
    if not ret:
        print(f"Could not find corners in {fname}")
        continue

    # 코너가 발견되면 포인트 저장 (store object points and image points)
    objpoints.append(objp)
    corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    imgpoints.append(corners2)

    # 코너 그리기 및 표시 (draw and display the corners)
    img = cv2.drawChessboardCorners(img, checkerboard_size, corners2, ret)
    cv2.imshow('img', img)
    cv2.waitKey(500)

cv2.destroyAllWindows()

# 카메라 캘리브레이션 수행 (camera calibration)
if gray is not None:
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    # 결과 출력 (print calibration results)
    if ret:
        print("Camera matrix:\n", mtx)
        print("Distortion coefficients:\n", dist)

        # 왜곡 제거 예제 (example: undistort images)
        for fname in images:
            img = cv2.imread(fname)
            h, w = img.shape[:2]
            new_camera_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

            # 왜곡 제거 (undistort)
            dst = cv2.undistort(img, mtx, dist, None, new_camera_mtx)

            # 결과 표시 (display undistorted image)
            cv2.imshow('Undistorted Image', dst)
            cv2.waitKey(500)

    cv2.destroyAllWindows()
else:
    print("Error: No valid gray image found for calibration.")
