#!/usr/bin/env python
import sys
import os
import time
import RPi.GPIO as GPIO

# SCServo and motor control imports
from scservo_sdk import *

# GPIO setup for air pump control
IN1 = 17  # GPIO pin connected to IN1 of L298N (Air pump)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(IN1, GPIO.OUT)

# Function to control the pump
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

# Initialize SCServo SDK
portHandler = PortHandler(DEVICENAME)
packetHandler = sms_sts(portHandler)

if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    quit()

if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()

def move_motor(position1, position2, position3, position4, position5, position6, speed1, speed2, speed3, speed4, speed5, speed6):
    """
    Function to move the motor to a given position.
    """
    if position1 < SCS_MINIMUM_POSITION_JOINT_VALUE or position1 > SCS_MAXIMUM_POSITION_JOINT_VALUE:
        print(f"Position1 {position1} out of bounds! Please provide a value between {SCS_MINIMUM_POSITION_JOINT_VALUE} and {SCS_MAXIMUM_POSITION_JOINT_VALUE}.")
        return
    if position2 < SCS_MINIMUM_POSITION_JOINT_VALUE or position2 > SCS_MAXIMUM_POSITION_JOINT_VALUE:
        print(f"Position2 {position2} out of bounds! Please provide a value between {SCS_MINIMUM_POSITION_JOINT_VALUE} and {SCS_MAXIMUM_POSITION_JOINT_VALUE}.")
        return
    if position3 < SCS_MINIMUM_POSITION_JOINT_VALUE or position3 > SCS_MAXIMUM_POSITION_JOINT_VALUE:
        print(f"Position3 {position3} out of bounds! Please provide a value between {SCS_MINIMUM_POSITION_JOINT_VALUE} and {SCS_MAXIMUM_POSITION_JOINT_VALUE}.")
        return
    if position4 < SCS_MINIMUM_POSITION_JOINT_VALUE or position4 > SCS_MAXIMUM_POSITION_JOINT_VALUE:
        print(f"Position4 {position4} out of bounds! Please provide a value between {SCS_MINIMUM_POSITION_JOINT_VALUE} and {SCS_MAXIMUM_POSITION_JOINT_VALUE}.")
        return
    if position5 < SCS_MINIMUM_POSITION_JOINT_VALUE or position5 > SCS_MAXIMUM_POSITION_JOINT_VALUE:
        print(f"Position5 {position5} out of bounds! Please provide a value between {SCS_MINIMUM_POSITION_JOINT_VALUE} and {SCS_MAXIMUM_POSITION_JOINT_VALUE}.")
        return
    if position6 < SCS_MINIMUM_POSITION_GRIPPER_VALUE or position6 > SCS_MAXIMUM_POSITION_GRIPPER_VALUE:
        print(f"Position6 {position6} out of bounds! Please provide a value between {SCS_MINIMUM_POSITION_GRIPPER_VALUE} and {SCS_MAXIMUM_POSITION_GRIPPER_VALUE}.")
        return

    scs_comm_result, scs_error = packetHandler.WritePosEx(SCS_ID0, position1, speed1, SCS_MOVING_ACC)
    scs_comm_result, scs_error = packetHandler.WritePosEx(SCS_ID1, position2, speed2, SCS_MOVING_ACC)
    scs_comm_result, scs_error = packetHandler.WritePosEx(SCS_ID2, 3845 - position2, speed2, SCS_MOVING_ACC)
    scs_comm_result, scs_error = packetHandler.WritePosEx(SCS_ID3, position3, speed3, SCS_MOVING_ACC)
    scs_comm_result, scs_error = packetHandler.WritePosEx(SCS_ID4, position4, speed4, SCS_MOVING_ACC)
    scs_comm_result, scs_error = packetHandler.WritePosEx(SCS_ID5, position5, speed5, SCS_MOVING_ACC)
    scs_comm_result, scs_error = packetHandler.WritePosEx(SCS_ID6, position6, speed6, SCS_MOVING_ACC)

    if scs_comm_result != COMM_SUCCESS:
        print(f"Error: {packetHandler.getTxRxResult(scs_comm_result)}")
    if scs_error != 0:
        print(f"Error: {packetHandler.getRxPacketError(scs_error)}")

# Main control loop
while True:
    print("Enter a position (0 to 2047) for the motor, or type 'exit' to quit:")
    
    # Take user input for motor positions and speeds
    print("**Joint1 -> 1023 = Left, 2047 = Middle, 3071 = Right**")
    user_pos1 = input("Joint1 pos : ")
    user_speed1 = input("Joint1 speed : ")

    print("**Joint2 -> 1023 = Front, 2047 = Middle, 3071 = Back**")
    user_pos2 = input("Joint2 pos : ")
    user_speed2 = input("Joint2 speed : ")

    print("**Joint3 -> 1023 = Back, 2047 = Middle, 3071 = Front**")
    user_pos3 = input("Joint3 pos : ")
    user_speed3 = input("Joint3 speed : ")

    print("**Joint4 -> 1023 = Front, 2047 = Middle, 3071 = Back**")
    user_pos4 = input("Joint4 pos : ")
    user_speed4 = input("Joint4 speed : ")

    print("**Joint5 -> 1023 = Left, 2200 = Middle, 3071 = Right**")
    user_pos5 = input("Joint5 pos : ")
    user_speed5 = input("Joint5 speed : ")

    print("**Gripper Range 1700 ~ 2300**")
    user_pos6 = input("Gripper pos : ")
    user_speed6 = input("Gripper speed : ")

    # Control the air pump based on user input
    user_pump = input("Do you want to turn the pump ON or OFF? (Enter 'on' or 'off'): ")
    if user_pump.lower() == "on":
        pump_on()
    elif user_pump.lower() == "off":
        pump_off()

    if user_pos1.lower() == "exit":
        break

    try:
        position1 = int(user_pos1)
        speed1 = int(user_speed1)
        position2 = int(user_pos2)
        speed2 = int(user_speed2)
        position3 = int(user_pos3)
        speed3 = int(user_speed3)
        position4 = int(user_pos4)
        speed4 = int(user_speed4)
        position5 = int(user_pos5)
        speed5 = int(user_speed5)
        position6 = int(user_pos6)
        speed6 = int(user_speed6)
        move_motor(position1, position2, position3, position4, position5, position6, speed1, speed2, speed3, speed4, speed5, speed6)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        
# Close port and cleanup GPIO
portHandler.closePort()
GPIO.cleanup()
