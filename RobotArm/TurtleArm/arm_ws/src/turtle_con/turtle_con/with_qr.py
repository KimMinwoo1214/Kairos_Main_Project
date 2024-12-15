#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from trajectory_msgs.msg import JointTrajectory
import RPi.GPIO as GPIO
from scservo_sdk import *
import math

# GPIO setup for air pump control
IN1 = 17  # GPIO pin connected to IN1 of L298N (Air pump)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(IN1, GPIO.OUT)

def pump_on():
    GPIO.output(IN1, GPIO.HIGH)
    print("Pump is ON")

def pump_off():
    GPIO.output(IN1, GPIO.LOW)
    print("Pump is OFF")

# Default SCServo settings
SCS_ID0 = 0
SCS_ID1 = 1
SCS_ID2 = 2
SCS_ID3 = 3
SCS_ID4 = 4
SCS_ID5 = 5
SCS_ID6 = 6
BAUDRATE = 1000000
DEVICENAME = '/dev/ttyAMA1'

SCS_MINIMUM_POSITION_JOINT_VALUE = 0
SCS_MAXIMUM_POSITION_JOINT_VALUE = 4095
SCS_MINIMUM_POSITION_GRIPPER_VALUE = 1700
SCS_MAXIMUM_POSITION_GRIPPER_VALUE = 2290
SCS_MOVING_ACC = 0  # SCServo moving acceleration

class JointControlNode(Node):
    def __init__(self):
        super().__init__('joint_control_node')
        
        # Initialize SCServo SDK
        self.portHandler = PortHandler(DEVICENAME)
        self.packetHandler = sms_sts(self.portHandler)

        if self.portHandler.openPort():
            self.get_logger().info("Succeeded to open the port")
        else:
            self.get_logger().error("Failed to open the port")
            self.destroy_node()

        if self.portHandler.setBaudRate(BAUDRATE):
            self.get_logger().info("Succeeded to change the baudrate")
        else:
            self.get_logger().error("Failed to change the baudrate")
            self.destroy_node()

        # Subscribe to joint control commands (String)
        self.joint_sub = self.create_subscription(
            String,
            '/joint_control',
            self.joint_control_callback,
            10
        )

        # Subscribe to pump control commands (String)
        self.pump_sub = self.create_subscription(
            String,
            '/pump_control',
            self.pump_control_callback,
            10
        )
        
        # Subscribe to trajectory commands (JointTrajectory)
        self.trajectory_sub = self.create_subscription(
            JointTrajectory,
            '/arm_controller/command',  # 필요에 따라 토픽 이름 변경 가능
            self.trajectory_callback,
            10
        )
        
    def pump_control_callback(self, msg):
        command = msg.data.strip().lower()
        if command == 'on':
            pump_on()
        elif command == 'off':
            pump_off()
        else:
            self.get_logger().warn("Unknown pump command received.")

    def joint_control_callback(self, msg):
        # Expecting a string like: "pos1 speed1 pos2 speed2 pos3 speed3 pos4 speed4 pos5 speed5 pos6 speed6"
        data = msg.data.strip().split()
        if len(data) != 12:
            self.get_logger().error("Invalid joint control command format.")
            return
        
        try:
            position1 = int(data[0])
            speed1 = int(data[1])
            position2 = int(data[2])
            speed2 = int(data[3])
            position3 = int(data[4])
            speed3 = int(data[5])
            position4 = int(data[6])
            speed4 = int(data[7])
            position5 = int(data[8])
            speed5 = int(data[9])
            position6 = int(data[10])
            speed6 = int(data[11])
        except ValueError:
            self.get_logger().error("Invalid values in joint control command (not integers).")
            return

        self.move_motor(position1, position2, position3, position4, position5, position6, 
                        speed1, speed2, speed3, speed4, speed5, speed6)

    def trajectory_callback(self, msg):
        # JointTrajectory 메시지를 수신하면, 첫 번째 point를 사용해 모터를 이동
        if len(msg.points) == 0:
            self.get_logger().error("Received empty trajectory message")
            return

        # 첫 번째 point 사용
        point = msg.points[0]
        positions = point.positions

        # 최소 6개 조인트 정보 있다고 가정 (6번째는 PWM 값)
        if len(positions) < 6:
            self.get_logger().error("Not enough joint positions in trajectory point")
            return

        # 라디안 값을 서보 포지션(PWM)으로 매핑
        def map_radian_to_pwm(radian, min_val=SCS_MINIMUM_POSITION_JOINT_VALUE, max_val=SCS_MAXIMUM_POSITION_JOINT_VALUE):
            # rad: [-pi, pi] -> [0, 4095]
            angle_normalized = (radian + math.pi) / (2 * math.pi)
            pwm = int(angle_normalized * (max_val - min_val))
            pwm = max(min_val, min(pwm, max_val))
            return pwm

        # 1~5번 조인트: 라디안 -> PWM
        position1 = map_radian_to_pwm(positions[0])
        position2 = map_radian_to_pwm(positions[1])
        position3 = map_radian_to_pwm(positions[2])
        position4 = map_radian_to_pwm(positions[3])
        position5 = map_radian_to_pwm(positions[4])

        # 6번 조인트: 이미 PWM 값이라고 가정 (라디안 변환 없음)
        try:
            position6 = int(positions[5])  # positions[5]는 이미 PWM 값
        except ValueError:
            self.get_logger().error("6th joint value (gripper) is not an integer PWM value.")
            return

        # 속도는 간단히 모두 100으로 가정
        speed1 = speed2 = speed3 = speed4 = speed5 = speed6 = 100

        self.move_motor(position1, position2, position3, position4, position5, position6,
                        speed1, speed2, speed3, speed4, speed5, speed6)

    def move_motor(self, position1, position2, position3, position4, position5, position6, 
                   speed1, speed2, speed3, speed4, speed5, speed6):
        """
        Move the motor to the given positions with given speeds.
        """
        # Check bounds
        if not (SCS_MINIMUM_POSITION_JOINT_VALUE <= position1 <= SCS_MAXIMUM_POSITION_JOINT_VALUE):
            self.get_logger().error("Position1 out of bounds")
            return
        if not (SCS_MINIMUM_POSITION_JOINT_VALUE <= position2 <= SCS_MAXIMUM_POSITION_JOINT_VALUE):
            self.get_logger().error("Position2 out of bounds")
            return
        if not (SCS_MINIMUM_POSITION_JOINT_VALUE <= position3 <= SCS_MAXIMUM_POSITION_JOINT_VALUE):
            self.get_logger().error("Position3 out of bounds")
            return
        if not (SCS_MINIMUM_POSITION_JOINT_VALUE <= position4 <= SCS_MAXIMUM_POSITION_JOINT_VALUE):
            self.get_logger().error("Position4 out of bounds")
            return
        if not (SCS_MINIMUM_POSITION_JOINT_VALUE <= position5 <= SCS_MAXIMUM_POSITION_JOINT_VALUE):
            self.get_logger().error("Position5 out of bounds")
            return
        if not (SCS_MINIMUM_POSITION_GRIPPER_VALUE <= position6 <= SCS_MAXIMUM_POSITION_GRIPPER_VALUE):
            self.get_logger().error("Position6(gripper) out of bounds")
            return
        
        # Write positions
        scs_comm_result, scs_error = self.packetHandler.WritePosEx(SCS_ID0, position1, speed1, SCS_MOVING_ACC)
        scs_comm_result, scs_error = self.packetHandler.WritePosEx(SCS_ID1, position2, speed2, SCS_MOVING_ACC)
        scs_comm_result, scs_error = self.packetHandler.WritePosEx(SCS_ID2, 3845 - position2, speed2, SCS_MOVING_ACC)
        scs_comm_result, scs_error = self.packetHandler.WritePosEx(SCS_ID3, position3, speed3, SCS_MOVING_ACC)
        scs_comm_result, scs_error = self.packetHandler.WritePosEx(SCS_ID4, position4, speed4, SCS_MOVING_ACC)
        scs_comm_result, scs_error = self.packetHandler.WritePosEx(SCS_ID5, position5, speed5, SCS_MOVING_ACC)
        scs_comm_result, scs_error = self.packetHandler.WritePosEx(SCS_ID6, position6, speed6, SCS_MOVING_ACC)

        if scs_comm_result != COMM_SUCCESS:
            self.get_logger().error(f"Communication Error: {self.packetHandler.getTxRxResult(scs_comm_result)}")
        if scs_error != 0:
            self.get_logger().error(f"Packet Error: {self.packetHandler.getRxPacketError(scs_error)}")

    def destroy_node(self):
        self.portHandler.closePort()
        GPIO.cleanup()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = JointControlNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down node.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
