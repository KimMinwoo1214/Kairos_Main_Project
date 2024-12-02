import RPi.GPIO as GPIO
import time

# Define GPIO pins
IN1 = 17  # GPIO pin connected to IN1 of L298N

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(IN1, GPIO.OUT)

# Functions to control the pump
def pump_on():
    GPIO.output(IN1, GPIO.HIGH)
    print("Pump is ON")

def pump_off():
    GPIO.output(IN1, GPIO.LOW)
    print("Pump is OFF")

try:
    while True:
        pump_on()  # Turn pump on
        time.sleep(5)  # Pump runs for 5 seconds
        pump_off()  # Turn pump off
        time.sleep(5)  # Pump is off for 5 seconds

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    GPIO.cleanup()  # Reset GPIO pins
