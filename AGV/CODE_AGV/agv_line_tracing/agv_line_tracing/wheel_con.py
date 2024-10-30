#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

HEADER = 0xFE
obstacle_detected = False  # 장애물 감지 플래그
last_command = None  # 마지막 실행 명령 저장

class WheelController(Node):
    def __init__(self):
        super().__init__('wheel_controller')
        
        # Serial port 설정 (포트 이름을 상황에 맞게 수정)
        self.port = serial.Serial(port="/dev/ttyAMA2", baudrate=115200, timeout=0.1)
        time.sleep(2)  # Serial 포트 초기화 대기

        # Teleop과 Obstacle 토픽 구독
        self.teleop_subscription = self.create_subscription(
            String, 'teleop_commands', self.teleop_callback, 10
        )
        self.obstacle_subscription = self.create_subscription(
            String, 'obstacle_detected', self.obstacle_detect_callback, 10
        )

    def send_wheel_command(self, direction_1, direction_2, direction_3):
        command = [
            HEADER,
            HEADER,
            direction_1,
            direction_2,
            direction_3,
            (direction_1 + direction_2 + direction_3) & 0xFF  # Checksum
        ]
        try:
            self.port.write(bytearray(command))
            self.port.flush()
        except serial.SerialException as e:
            self.get_logger().error(f"Serial communication error: {e}")

    def teleop_callback(self, data):
        global obstacle_detected, last_command

        # 장애물 감지 상태 확인
        if obstacle_detected:
            # 장애물 감지 시 현재 명령을 저장하고 모든 모터를 정지
            last_command = data.data  # 마지막 명령을 저장
            self.get_logger().warn(f"Obstacle detected! Saving command '{last_command}' and stopping AGV.")
            self.send_wheel_command(128, 128, 128)
            return

        # 장애물이 없을 때만 teleop 명령 처리
        teleop_command = data.data
        self.get_logger().info(f"Received teleop command: {teleop_command}")
        last_command = teleop_command  # 마지막 명령을 저장

        if teleop_command == "forward":
            self.send_wheel_command(133, 128, 128)  # 전진 명령
        elif teleop_command == "cw":
            self.send_wheel_command(128, 128, 123)  # 시계 방향 회전 명령
        elif teleop_command == "ccw":
            self.send_wheel_command(128, 128, 133)  # 반시계 방향 회전 명령
        else:
            self.send_wheel_command(128, 128, 128)  # 정지 명령

    def obstacle_detect_callback(self, data):
        global obstacle_detected, last_command
        obstacle_detected = data.data == "true"
        self.get_logger().info(f"Obstacle detection updated: {obstacle_detected}")

        # 장애물 감지 시 즉시 정지 명령 전송
        if obstacle_detected:
            self.send_wheel_command(128, 128, 128)
            self.get_logger().info("Obstacle detected! AGV stopped immediately.")
        elif last_command:
            # 장애물이 사라졌을 때 마지막 명령을 다시 실행
            self.get_logger().info(f"Obstacle cleared, resuming last command: {last_command}")
            if last_command == "forward":
                self.send_wheel_command(158, 128, 128)  # 전진 명령
            elif last_command == "cw":
                self.send_wheel_command(128, 158, 128)  # 시계 방향 회전 명령
            elif last_command == "ccw":
                self.send_wheel_command(128, 128, 158)  # 반시계 방향 회전 명령
            else:
                self.send_wheel_command(128, 128, 128)  # 정지 명령

def main(args=None):
    rclpy.init(args=args)
    wheel_controller = WheelController()
    rclpy.spin(wheel_controller)

    # 종료 시 정지 명령 전송
    wheel_controller.send_wheel_command(128, 128, 128)
    if wheel_controller.port.is_open:
        wheel_controller.port.close()

    rclpy.shutdown()

if __name__ == "__main__":
    main()
