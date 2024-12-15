# File: udp_video_server.py
import cv2
import imutils
import socket
import numpy as np
import time
import base64

BUFF_SIZE = 65536
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
host_name = socket.gethostname()
host_ip = '192.168.0.198'  # Replace with your server's IP
port = 9090
socket_address = (host_ip, port)
server_socket.bind(socket_address)
print('Listening at:', socket_address)

vid = cv2.VideoCapture(0)  # Replace 'rocket.mp4' with 0 for webcam
fps, st, frames_to_count, cnt = (0, 0, 20, 0)

# Camera calibration parameters
mtx = np.array([[317.05966638, 0., 287.9901831],
                [0., 317.21510719, 232.81085565],
                [0., 0., 1.]])  # Camera matrix
dist = np.array([-0.3063854, 0.10224856, 0.00108754, -0.00063471, -0.01660539])  # Distortion coefficients

while True:
    msg, client_addr = server_socket.recvfrom(BUFF_SIZE)
    print('GOT connection from ', client_addr)
    WIDTH = 400
    SCALE = 1.5  # Scale factor for resizing the frame
    while vid.isOpened():
        ret, frame = vid.read()
        if not ret:
            print("Failed to capture video frame")
            break

        # Rotate the frame by 180 degrees
        frame = cv2.rotate(frame, cv2.ROTATE_180)

        # Undistort the frame using the camera matrix and distortion coefficients
        h, w = frame.shape[:2]
        new_camera_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
        frame = cv2.undistort(frame, mtx, dist, None, new_camera_mtx)

        # Crop the image to remove black edges caused by distortion correction
        x, y, w, h = roi
        frame = frame[y:y+h, x:x+w]

        # Resize the frame to the desired width
        frame = imutils.resize(frame, width=WIDTH)

        # Scale the frame by 1.5x
        new_width = int(frame.shape[1] * SCALE)
        new_height = int(frame.shape[0] * SCALE)
        frame = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

        # Encode the frame
        encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        message = base64.b64encode(buffer)

        # Send the frame
        server_socket.sendto(message, client_addr)

        # Display FPS
        frame = cv2.putText(frame, 'FPS: ' + str(fps), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            server_socket.close()
            break

        # FPS calculation
        if cnt == frames_to_count:
            try:
                fps = round(frames_to_count / (time.time() - st))
                st = time.time()
                cnt = 0
            except ZeroDivisionError:
                pass
        cnt += 1
