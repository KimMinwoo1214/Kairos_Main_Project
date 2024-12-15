import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory
from sensor_msgs.msg import JointState
from scservo_sdk import *
import RPi.GPIO as GPIO
import time

# GPIO setup for air pump control
IN1 = 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(IN1, GPIO.OUT)

def pump_on():
    GPIO.output(IN1, GPIO.HIGH)
    print("Pump is ON")

def pump_off():
    GPIO.output(IN1, GPIO.LOW)
    print("Pump is OFF")

class RobotArmController(Node):
    def __init__(self):
        super().__init__('robot_arm_controller')

        # SCServo setup
        self.DEVICENAME = '/dev/ttyAMA1'
        self.BAUDRATE = 1000000
        self.SCS_MOVING_ACC = 0
        self.MIN_POSITION = 0
        self.MAX_POSITION = 4095

        # Map init_pose to radians
        self.INIT_POSE_RADIAN = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.INIT_PWM = [2047, 2095, 2040, 2058, 2230]

        self.port_handler = PortHandler(self.DEVICENAME)
        self.packet_handler = sms_sts(self.port_handler)

        if self.port_handler.openPort():
            self.get_logger().info("Succeeded to open the port")
        else:
            self.get_logger().error("Failed to open the port")
            self.destroy_node()

        if self.port_handler.setBaudRate(self.BAUDRATE):
            self.get_logger().info("Succeeded to set baudrate")
        else:
            self.get_logger().error("Failed to set baudrate")
            self.destroy_node()

        # ROS2 subscriptions
        self.trajectory_sub = self.create_subscription(
            JointTrajectory,
            '/arm_controller/command',
            self.trajectory_callback,
            10
        )

        self.joint_state_sub = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_state_callback,
            10
        )

    def joint_state_callback(self, msg):
        """
        Process joint states and map positions to servo ranges.
        """
        if len(msg.position) < 5:
            self.get_logger().error("Invalid joint state positions")
            return

        joint_positions = [
            self.map_radian_to_pwm(pos, self.INIT_POSE_RADIAN[i], self.INIT_PWM[i]) for i, pos in enumerate(msg.position[:5])
        ]

        # Get current positions of the motors
        current_positions = [
            self.get_current_position(motor_id) for motor_id in range(5)
        ]

        # Ensure all positions are integers
        joint_positions = [int(pos) if isinstance(pos, int) else int(pos[0]) for pos in joint_positions]
        current_positions = [int(pos) if isinstance(pos, int) else int(pos[0]) for pos in current_positions]

        # Calculate dynamic speeds based on PWM differences
        calculated_speeds = self.calculate_speeds(current_positions, joint_positions)

        # Move the motors with dynamic speeds
        self.move_motor(*joint_positions, *calculated_speeds)

    def trajectory_callback(self, msg):
        self.get_logger().info("Received trajectory command")
        if len(msg.points) == 0:
            self.get_logger().error("Trajectory message has no points")
            return

        for point in msg.points:
            positions = point.positions
            if len(positions) < 5:
                self.get_logger().error("Invalid number of joint positions in trajectory")
                continue

            # Map positions to SCServo PWM limits
            joint_positions = [
                self.map_radian_to_pwm(pos, self.INIT_POSE_RADIAN[i], self.INIT_PWM[i]) for i, pos in enumerate(positions[:5])
            ]

            # Get current positions of the motors
            current_positions = [
                self.get_current_position(motor_id) for motor_id in range(5)
            ]

            # Ensure all positions are integers
            joint_positions = [int(pos) if isinstance(pos, int) else int(pos[0]) for pos in joint_positions]
            current_positions = [int(pos) if isinstance(pos, int) else int(pos[0]) for pos in current_positions]

            # Calculate speeds based on PWM differences
            speeds = self.calculate_speeds(current_positions, joint_positions)

            # Move the motors
            self.move_motor(*joint_positions, *speeds)

            # Wait for the duration of this trajectory point
            target_time = point.time_from_start.sec + point.time_from_start.nanosec / 1e9
            time.sleep(target_time)

    def map_radian_to_pwm(self, radian, init_radian, init_pwm):
        """
        Map a radian value to servo PWM range based on init_pose.
        :param radian: Radian value (-pi to pi range)
        :param init_radian: The initial radian corresponding to init_pose
        :param init_pwm: The initial PWM value for init_pose
        :return: Mapped servo position value in PWM range
        """
        degrees = (radian - init_radian) * (180.0 / 3.141592653589793)
        if degrees > 0:
            return int(init_pwm + (self.MAX_POSITION - init_pwm) * (degrees / 180.0))
        else:
            return int(init_pwm + (self.MIN_POSITION - init_pwm) * (degrees / -180.0))

    def calculate_speeds(self, init_pwms, goal_pwms, base_speed=4095):
        """
        Calculate speeds for each motor based on PWM differences, reduced by half.
        :param init_pwms: List of initial PWM values.
        :param goal_pwms: List of goal PWM values.
        :param base_speed: The base speed for the smallest PWM difference.
        :return: List of calculated speeds for each motor.
        """
        pwm_differences = [abs(goal - init) for goal, init in zip(goal_pwms, init_pwms)]
        max_difference = max(pwm_differences)

        # Calculate speed proportional to the PWM difference and reduce it by half
        speeds = [
            int((diff / max_difference) * base_speed / 2) if max_difference > 0 else base_speed // 2
            for diff in pwm_differences
        ]

        return speeds

    def get_current_position(self, motor_id):
        """
        Get the current position of the motor.
        """
        try:
            position = self.packet_handler.ReadPos(motor_id)
            return int(position) if isinstance(position, int) else int(position[0])
        except Exception as e:
            self.get_logger().error(f"Failed to read position for motor {motor_id}: {e}")
            return 0

    def move_motor(self, pos1, pos2, pos3, pos4, pos5, spd1, spd2, spd3, spd4, spd5):
        self.packet_handler.WritePosEx(0, pos1, spd1, self.SCS_MOVING_ACC)
        self.packet_handler.WritePosEx(1, pos2, spd2, self.SCS_MOVING_ACC)
        self.packet_handler.WritePosEx(2, 3845 - pos2, spd2, self.SCS_MOVING_ACC)
        self.packet_handler.WritePosEx(3, pos3, spd3, self.SCS_MOVING_ACC)
        self.packet_handler.WritePosEx(4, pos4, spd4, self.SCS_MOVING_ACC)
        self.packet_handler.WritePosEx(5, pos5, spd5, self.SCS_MOVING_ACC)

    def close(self):
        self.port_handler.closePort()
        GPIO.cleanup()


def main(args=None):
    rclpy.init(args=args)
    controller = RobotArmController()

    try:
        rclpy.spin(controller)
    except KeyboardInterrupt:
        controller.get_logger().info("Shutting down robot arm controller")
    finally:
        controller.close()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
