# File: qr_code_detector_node.py

import cv2
import numpy as np
from pyzbar.pyzbar import decode
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class QRCodeDetectorNode(Node):
    def __init__(self):
        super().__init__('qr_code_detector')
        self.get_logger().info("Starting QR Code Detector Node")
        
        # Publisher for QR code data
        self.qr_code_publisher = self.create_publisher(String, 'qr_code_data', 10)

        # Desired QR code to trigger a stop
        self.desired_qr_code = "STOP_HERE"

        # Camera calibration matrix and distortion coefficients
        self.mtx = np.array([[317.05966638, 0., 287.9901831],
                             [0., 317.21510719, 232.81085565],
                             [0., 0., 1.]])  # Camera matrix

        self.dist = np.array([-0.3063854, 0.10224856, 0.00108754, -0.00063471, -0.01660539])  # Distortion coefficients

        # Open the camera
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.get_logger().error("Error: Could not open the camera")
            rclpy.shutdown()

        # ZOOM-IN settings
        self.zoom_factor = 2  # Initial ZOOM-IN factor
        self.zoom_mode = True  # Enable ZOOM-IN mode
        self.zoom_x1, self.zoom_y1, self.zoom_x2, self.zoom_y2 = 0, 0, 0, 0

        # Create a timer to process frames periodically
        self.timer = self.create_timer(0.1, self.process_frame)

    def process_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().error("Error: Could not read the frame")
            return

        # Undistort the captured frame
        undistorted_frame = cv2.undistort(frame, self.mtx, self.dist)

        # Flip the undistorted frame vertically
        flipped_frame = cv2.flip(undistorted_frame, 0)

        # Initial ZOOM-IN logic
        if self.zoom_mode and self.zoom_x1 == 0 and self.zoom_x2 == 0:  # Set ROI on the first frame
            h, w = flipped_frame.shape[:2]
            center_x, center_y = w // 2, h // 2  # Frame center
            half_w, half_h = int(w // (2 * self.zoom_factor)), int(h // (2 * self.zoom_factor))

            # Calculate initial zoomed ROI
            self.zoom_x1 = max(center_x - half_w, 0)
            self.zoom_y1 = max(center_y - half_h, 0)
            self.zoom_x2 = min(center_x + half_w, w)
            self.zoom_y2 = min(center_y + half_h, h)

        # Apply ZOOM-IN if zoom_mode is enabled
        if self.zoom_mode:
            zoomed_frame = flipped_frame[int(self.zoom_y1):int(self.zoom_y2), int(self.zoom_x1):int(self.zoom_x2)]
            if zoomed_frame.size > 0:
                flipped_frame = cv2.resize(zoomed_frame, (flipped_frame.shape[1], flipped_frame.shape[0]), interpolation=cv2.INTER_LINEAR)

        # Detect QR codes using pyzbar
        decoded_objects = decode(flipped_frame)
        for obj in decoded_objects:
            qr_data = obj.data.decode("utf-8")
            self.get_logger().info(f"Detected QR Code: {qr_data}")

            # Publish the QR code data
            msg = String()
            msg.data = qr_data
            self.qr_code_publisher.publish(msg)

            # Check if the detected QR code matches the desired QR code
            if qr_data == self.desired_qr_code:
                self.get_logger().info("Desired QR code detected! Publishing stop signal.")
                stop_msg = String()
                stop_msg.data = "STOP_SIGNAL"
                self.qr_code_publisher.publish(stop_msg)

    def destroy_node(self):
        self.cap.release()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = QRCodeDetectorNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
