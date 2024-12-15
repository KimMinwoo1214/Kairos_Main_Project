import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory
from sensor_msgs.msg import JointState
from std_msgs.msg import String
from scservo_sdk import *
import RPi.GPIO as GPIO

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

        # Initial joint positions and PWM mappings
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
        self.qr_data_sub = self.create_subscription(
            String,
            '/qr_code_data',
            self.qr_code_callback,
            10
        )

        self.joint_state_sub = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_state_callback,
            10
        )

        self.current_joint_positions = [0.0, 0.0, 0.0, 0.0, 0.0]

    def qr_code_callback(self, msg):
        """
        Callback for QR code data. 
        """
        qr_data = msg.data.strip()
        self.get_logger().info(f"QR Code Received: {qr_data}")
        # 정지 로직 제거됨

    def joint_state_callback(self, msg):
        """
        Process joint states and map positions to servo ranges.
        """
        if len(msg.position) < 5:
            self.get_logger().error("Invalid joint state positions")
            return

        self.current_joint_positions = msg.position[:5]
        joint_positions = [
            self.map_radian_to_pwm(pos, self.INIT_POSE_RADIAN[i], self.INIT_PWM[i]) 
            for i, pos in enumerate(self.current_joint_positions)
        ]

        current_positions = [
            self.get_current_position(motor_id) for motor_id in range(5)
        ]

        calculated_speeds = self.calculate_speeds(current_positions, joint_positions)

        self.move_motor(
            joint_positions[0], joint_positions[1], joint_positions[2],
            joint_positions[3], joint_positions[4],
            spd1=calculated_speeds[0], spd2=calculated_speeds[1],
            spd3=calculated_speeds[2], spd4=calculated_speeds[3],
            spd5=calculated_speeds[4]
        )

    def calculate_speeds(self, init_pwms, goal_pwms, base_speed=4095):
        """
        Calculate speeds for each motor based on PWM differences.
        """
        pwm_differences = [abs(goal - init) for goal, init in zip(goal_pwms, init_pwms)]
        max_difference = max(pwm_differences)

        speeds = [
            int((diff / max_difference) * base_speed / 2) if max_difference > 0 else base_speed // 2
            for diff in pwm_differences
        ]

        for i in range(5):
            if i == 4:
                speeds[i] = speeds[i] // 12
            else:
                speeds[i] = speeds[i] // 8

        return speeds

    def map_radian_to_pwm(self, radian, init_radian, init_pwm):
        degrees = (radian - init_radian) * (180.0 / 3.141592653589793)
        if degrees > 0:
            return int(init_pwm + (self.MAX_POSITION - init_pwm) * (degrees / 180.0))
        else:
            return int(init_pwm + (self.MIN_POSITION - init_pwm) * (degrees / -180.0))

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
        """
        Move motors to the specified positions with the specified speeds.
        """
        try:
            if spd1 > 0:
                self.packet_handler.WritePosEx(0, pos1, spd1, self.SCS_MOVING_ACC)
            if spd2 > 0:
                self.packet_handler.WritePosEx(1, pos2, spd2, self.SCS_MOVING_ACC)
            if spd3 > 0:
                self.packet_handler.WritePosEx(2, 3845 - pos3, spd3, self.SCS_MOVING_ACC)
            if spd4 > 0:
                self.packet_handler.WritePosEx(3, pos4, spd4, self.SCS_MOVING_ACC)
            if spd5 > 0:
                self.packet_handler.WritePosEx(4, pos5, spd5, self.SCS_MOVING_ACC)
        except Exception as e:
            self.get_logger().error(f"Failed to move motors: {e}")

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
