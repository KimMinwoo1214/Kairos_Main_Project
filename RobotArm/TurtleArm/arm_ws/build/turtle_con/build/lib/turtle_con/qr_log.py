import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
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

        # ROS2 subscription to receive trajectory commands from BT
        self.trajectory_sub = self.create_subscription(
            JointTrajectory,
            '/arm_controller/command',
            self.trajectory_callback,
            10
        )

        # Initialize current joint states
        self.current_joint_angles = [0.0] * 5

    def trajectory_callback(self, msg):
        """
        Handle trajectory commands and move motors.
        """
        if len(msg.points) == 0:
            self.get_logger().error("Trajectory message has no points")
            return

        for point in msg.points:
            positions = point.positions
            if len(positions) < 5:
                self.get_logger().error("Invalid number of joint positions in trajectory")
                continue

            # Convert positions (radians) to PWM and move motors
            joint_positions = [
                self.map_radian_to_pwm(pos, self.current_joint_angles[i], 2047) for i, pos in enumerate(positions[:5])
            ]

            self.get_logger().info(f"Moving to joint positions (PWM): {joint_positions}")
            self.move_motor(
                joint_positions[0], joint_positions[1], joint_positions[2],
                joint_positions[3], joint_positions[4],
                spd1=512, spd2=512, spd3=512, spd4=512, spd5=512
            )

    def move_motor(self, pos1, pos2, pos3, pos4, pos5, spd1, spd2, spd3, spd4, spd5):
        """
        Send commands to motors to move to the desired positions.
        """
        self.packet_handler.WritePosEx(0, pos1, spd1, self.SCS_MOVING_ACC)
        self.packet_handler.WritePosEx(1, pos2, spd2, self.SCS_MOVING_ACC)
        self.packet_handler.WritePosEx(2, 3845 - pos2, spd2, self.SCS_MOVING_ACC)
        self.packet_handler.WritePosEx(3, pos3, spd3, self.SCS_MOVING_ACC)
        self.packet_handler.WritePosEx(4, pos4, spd4, self.SCS_MOVING_ACC)
        self.packet_handler.WritePosEx(5, pos5, spd5, self.SCS_MOVING_ACC)

    def map_radian_to_pwm(self, radian, init_radian, init_pwm):
        """
        Map radian values to servo PWM range.
        """
        degrees = (radian - init_radian) * (180.0 / 3.141592653589793)
        if degrees > 0:
            return int(init_pwm + (self.MAX_POSITION - init_pwm) * (degrees / 180.0))
        else:
            return int(init_pwm + (self.MIN_POSITION - init_pwm) * (degrees / -180.0))

    def close(self):
        """
        Close the port and clean up GPIO.
        """
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
