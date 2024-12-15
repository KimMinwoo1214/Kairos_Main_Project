import cv2
import numpy as np
import serial
import time
import tkinter as tk
from tkinter import ttk
import threading

# Camera matrix and distortion coefficients from your calibration
mtx = np.array([[310.93505147, 0., 305.1882977],
                [0., 311.02060429, 238.72764315],
                [0., 0., 1.]])  # Camera matrix

dist = np.array([-3.42750945e-01,  1.49543845e-01,  2.39640046e-04,  4.72473300e-04, -3.54611271e-02])  # Distortion coefficients

# Serial connection settings
#port = '/dev/ttyUSB0'  # Adjust based on your port
#baudrate = 1000000
#ser = serial.Serial(port, baudrate)
#time.sleep(2)  # Wait for Arduino to initialize

# Global variables for sliders
slider0 = slider1 = slider2 = slider3 = None
angle0_label = angle1_label = angle2_label = angle3_label = None

# Function to handle webcam capture and undistortion
def webcam_thread():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return
    
    cv2.namedWindow("Live Video", cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame")
            break

        # Undistort the captured frame using the camera matrix and distortion coefficients
        undistorted_frame = cv2.undistort(frame, mtx, dist)

        # Display the undistorted frame
        cv2.imshow("Live Video - Undistorted", undistorted_frame)

        # Press 'q' to quit the live video feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to update servo angles via serial communication
def update_servo_angles():
    angle0 = slider0.get()
    angle1 = slider1.get()
    angle2 = slider2.get()
    angle3 = slider3.get()

    # Send angles to Arduino via serial
    ser.write(f"{angle0},{angle1},{angle2},{angle3}\n".encode('utf-8'))

    # Update angle labels in the Tkinter GUI
    angle0_label.config(text=f"각도 0: {int(angle0)}")
    angle1_label.config(text=f"각도 1: {int(angle1)}")
    angle2_label.config(text=f"각도 2: {int(angle2)}")
    angle3_label.config(text=f"각도 3: {int(angle3)}")

# Function to stop all servos and set them to default position
def stop_all_servos():
    slider0.set(2048)
    slider1.set(2048)
    slider2.set(2048)
    slider3.set(2048)

    # Send stop command to Arduino
    ser.write(f"2048,2048,2048,2048\n".encode('utf-8'))

    # Update angle labels
    angle0_label.config(text=f"각도 0: 2048")
    angle1_label.config(text=f"각도 1: 2048")
    angle2_label.config(text=f"각도 2: 2048")
    angle3_label.config(text=f"각도 3: 2048")

# Tkinter UI setup
def setup_gui():
    global slider0, slider1, slider2, slider3
    global angle0_label, angle1_label, angle2_label, angle3_label

    root = tk.Tk()
    root.title("서보 모터 각도 조정")

    # Create and pack the sliders and labels for controlling the servos
    label0 = ttk.Label(root, text="첫 번째 서보 각도")
    label0.pack(pady=10)
    slider0 = ttk.Scale(root, from_=0, to_=4095, orient="horizontal", length=300)
    slider0.set(2048)
    slider0.pack()
    angle0_label = ttk.Label(root, text=f"각도 1: {int(slider0.get())}")
    angle0_label.pack()

    label1 = ttk.Label(root, text="첫 번째 서보 각도")
    label1.pack(pady=10)
    slider1 = ttk.Scale(root, from_=800, to_=3100, orient="horizontal", length=300)
    slider1.set(2048)
    slider1.pack()
    angle1_label = ttk.Label(root, text=f"각도 1: {int(slider1.get())}")
    angle1_label.pack()

    label2 = ttk.Label(root, text="두 번째 서보 각도")
    label2.pack(pady=10)
    slider2 = ttk.Scale(root, from_=250, to_=3500, orient="horizontal", length=300)
    slider2.set(2048)
    slider2.pack()
    angle2_label = ttk.Label(root, text=f"각도 2: {int(slider2.get())}")
    angle2_label.pack()

    label3 = ttk.Label(root, text="세 번째 서보 각도")
    label3.pack(pady=10)
    slider3 = ttk.Scale(root, from_=0, to_=4095, orient="horizontal", length=300)
    slider3.set(2048)
    slider3.pack()
    angle3_label = ttk.Label(root, text=f"각도 3: {int(slider3.get())}")
    angle3_label.pack()

    # Update labels when sliders move
    slider0.bind("<Motion>", lambda event: angle0_label.config(text=f"각도 0: {int(slider0.get())}"))
    slider1.bind("<Motion>", lambda event: angle1_label.config(text=f"각도 1: {int(slider1.get())}"))
    slider2.bind("<Motion>", lambda event: angle2_label.config(text=f"각도 2: {int(slider2.get())}"))
    slider3.bind("<Motion>", lambda event: angle3_label.config(text=f"각도 3: {int(slider3.get())}"))

    # Buttons to update servo angles and stop servos
    update_button = ttk.Button(root, text="서보 각도 전송", command=update_servo_angles)
    update_button.pack(pady=20)

    stop_button = ttk.Button(root, text="Stop (모두 2048로 설정)", command=stop_all_servos)
    stop_button.pack(pady=20)

    root.mainloop()

# Start both threads (webcam and GUI)
if __name__ == "__main__":
    # Start the webcam thread
    webcam_thread = threading.Thread(target=webcam_thread)
    webcam_thread.daemon = True  # Daemonize the thread so it exits when the main program exits
    webcam_thread.start()

    # Start the Tkinter GUI
    setup_gui()
    
    # Close serial connection properly when the program exits
    ser.close()
