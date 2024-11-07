import cv2
import numpy as np
import time
from threading import Thread, Lock
from pymycobot.myagv import MyAgv
import pyzbar.pyzbar as pyzbar
import rplidar

# 전역 변수
offset_lock = Lock()  # 오프셋 값 보호용 락
offset = 0  # 중심에서의 오프셋 값 저장
motor_running = False
frame_lock = Lock()  # 프레임 보호용 락
line_frame = None  # 라인 감지용 비디오 프레임 저장 변수
qr_frame = None  # QR 코드 인식을 위한 비디오 프레임 저장 변수
udp_run = True  # 실행 플래그
qr_data = None  # QR 코드 데이터 저장 변수
detected_data = None

class VideoProcessingThread(Thread):
    def __init__(self, width):
        Thread.__init__(self)
        self.width = width
        self.vid = cv2.VideoCapture(0)
    
        # 비디오 저장 객체 생성
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.line_video_writer = cv2.VideoWriter('line_detection_output.avi', fourcc, 20, (width, int(width * 0.75 * 2 // 5)))
        self.qr_video_writer = cv2.VideoWriter('qr_detection_output.avi', fourcc, 20, (width, int(width * 0.75)))

    def run(self):
        global line_frame, qr_frame, offset, udp_run, motor_running, qr_data, detected_data

        while udp_run:
            ret, new_frame = self.vid.read()
            if ret:
                new_frame = cv2.resize(new_frame, (self.width, int(self.width * 0.75)))
                height, width, _ = new_frame.shape
                # 라인 감지용 프레임과 QR 코드 인식을 위한 프레임 분리
                with frame_lock:
                    line_frame = new_frame[height * 3 // 5:, :].copy()  # 라인 감지용 프레임 하단 2/5 부분
                    qr_frame = new_frame.copy()  # QR 코드 인식을 위한 프레임

                # QR 코드 감지
                decoded_objects = pyzbar.decode(qr_frame)
                if decoded_objects:
                    print("QR 코드 감지됨. AGV 정지.")
                    
                    for obj in decoded_objects:
                        detected_data = obj.data.decode('utf-8')
                        print("QR 코드 데이터:", detected_data)
                        (x, y, w, h) = obj.rect
                        # QR 코드 주변에 녹색 상자 그리기
                        cv2.rectangle(qr_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        if detected_data == qr_data:
                            motor_running = True

                # 빨간색 감지 및 오프셋 계산
                img_hsv = cv2.cvtColor(line_frame, cv2.COLOR_BGR2HSV)
                lower_red1 = np.array([0, 50, 50])
                upper_red1 = np.array([10, 255, 255])
                lower_red2 = np.array([170, 50, 50])
                upper_red2 = np.array([180, 255, 255])

                mask1 = cv2.inRange(img_hsv, lower_red1, upper_red1)
                mask2 = cv2.inRange(img_hsv, lower_red2, upper_red2)
                mask = mask1 + mask2

                kernel = np.ones((5, 5), np.uint8)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

                # 윤곽선 감지
                contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                if contours:
                    max_contour = max(contours, key=cv2.contourArea)
                    if cv2.contourArea(max_contour) > 1000:
                        cv2.drawContours(line_frame, [max_contour], -1, (0, 255, 0), 2)
                        x, y, w, h = cv2.boundingRect(max_contour)
                        cv2.rectangle(line_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        M = cv2.moments(max_contour)
                        if M["m00"] != 0:
                            cx = int(M["m10"] / M["m00"])
                            cy = int(M["m01"] / M["m00"])
                            cv2.circle(line_frame, (cx, cy), 10, (0, 255, 0), -1)

                            # 중심 오프셋 계산
                            with offset_lock:
                                offset = cx - width // 2
                            print(f"Calculated offset: {offset}")
                else:
                    print("no find line")
                    motor_running = False
                    time.sleep(0.2)
                    offset = -900
                
                # 비디오 파일로 저장
                self.line_video_writer.write(line_frame)
                self.qr_video_writer.write(qr_frame)
                
        self.vid.release()
        self.line_video_writer.release()
        self.qr_video_writer.release()

class AgvControlThread(Thread):
    def __init__(self, myagv):
        Thread.__init__(self)
        self.myagv = myagv
    
    def run(self):
        global offset, motor_running, udp_run, qr_data, detected_data

        while udp_run:
            with offset_lock:
                current_offset = offset
                if motor_running and qr_data == '1' and detected_data == '1':
                    print("QR 코드 데이터가 '1'입니다. AGV CORNERING 중.")
                    self.myagv.go_ahead(5, 2)
                    self.myagv.counterclockwise_rotation(5, 3.5)
                    qr_data = None  # QR 데이터 초기화
                    detected_data = None
                elif motor_running and qr_data == '2' and detected_data == '2':
                    print("QR 코드 데이터가 '2'입니다. AGV CORNERING 중.")
                    self.myagv.go_ahead(5, 2)
                    self.myagv.counterclockwise_rotation(5, 3)
                    qr_data = None
                    detected_data = None
                elif motor_running and qr_data == '3' and detected_data == '3':
                    print("QR 코드 데이터가 '3'입니다. AGV CORNERING 중.")
                    self.myagv.go_ahead(5, 2.5)
                    self.myagv.counterclockwise_rotation(5, 3)
                    qr_data = None
                    detected_data = None
                elif motor_running and 800 > current_offset > 30:
                    print(f"Object is {current_offset} pixels to the right. Moving AGV left.")
                    self.myagv.clockwise_rotation(5, 0.2)
                elif motor_running and -800<current_offset < -30:
                    print(f"Object is {-current_offset} pixels to the left. Moving AGV right.")
                    self.myagv.counterclockwise_rotation(5, 0.2)
                elif motor_running and -30 <= current_offset <= 30:
                    print('Object is centered. Moving AGV forward.')
                    self.myagv._mesg(128+8, 128, 128)
                else:
                    self.myagv.stop()

            time.sleep(0.2)

def main():
    global motor_running, udp_run, line_frame, qr_frame, qr_data

    # MyAGV 객체 생성
    myagv = MyAgv('/dev/ttyAMA2', 115200)

    # 영상 처리 스레드 시작
    video_thread = VideoProcessingThread(400)
    video_thread.daemon = True
    video_thread.start()

    # AGV 제어 스레드 시작
    agv_thread = AgvControlThread(myagv)
    agv_thread.daemon = True
    agv_thread.start()

    # 메인 루프 - 키보드 입력 및 영상 출력
    while True:
        key = cv2.waitKey(10) & 0xFF
        if key == ord('1') and not motor_running:
            print("Key '1' pressed. Starting the motor for QR code data '1'.")
            motor_running = True
            qr_data = '1'
        elif key == ord('2')and not motor_running:
            print("Key '2' pressed. Starting the motor for QR code data '2'.")
            motor_running = True
            qr_data = '2'
        elif key == ord('3') and not motor_running :
            print("Key '3' pressed. Starting the motor for QR code data '3'.")
            motor_running = True
            qr_data = '3'
        elif key == ord('s') and motor_running:
            print("Key 's' pressed. Stopping the motor.")
            motor_running = False
            qr_data = None  # QR 데이터 초기화
            myagv.stop()  # AGV 멈춤 명령
        elif key == ord('q'):
            print("Exiting program...")
            udp_run = False
            myagv.stop()
            break

        # 프레임을 메인 스레드에서 표시
        with frame_lock:
            if line_frame is not None:
                cv2.imshow('Line Detection Video', line_frame)
            if qr_frame is not None:
                cv2.imshow('QR Detection Video', qr_frame)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
