import cv2
import numpy as np
import time
from threading import Thread, Lock
from pymycobot.myagv import MyAgv
import pyzbar.pyzbar as pyzbar

# 전역 변수
offset_lock = Lock()  # 오프셋 값 보호용 락
offset = 0  # 중심에서의 오프셋 값 저장
motor_running = True  # 기본적으로 노란색 선 추적을 활성화
udp_run = True  # 실행 플래그
qr_data = None  # QR 코드 데이터 저장 변수
detected_data = None
rotation_sequence_active = False  # 회전 시퀀스 활성화 플래그

class VideoProcessingThread(Thread):
    def __init__(self, width, myagv):
        Thread.__init__(self)
        self.width = width
        self.vid = cv2.VideoCapture(2)
        self.myagv = myagv  # MyAgv 객체를 VideoProcessingThread에 전달

    def run(self):
        global offset, udp_run, motor_running, qr_data, detected_data, rotation_sequence_active

        while udp_run:
            ret, new_frame = self.vid.read()
            if ret:
                new_frame = cv2.resize(new_frame, (self.width, int(self.width * 0.75)))
                height, width, _ = new_frame.shape
                line_frame = new_frame[height * 3 // 5:, :].copy()  # 라인 감지용 프레임 하단 2/5 부분
                qr_frame = new_frame.copy()  # QR 코드 인식을 위한 프레임

                # HSV 색상 공간 변환
                img_hsv = cv2.cvtColor(line_frame, cv2.COLOR_BGR2HSV)

                # 파란색 영역 감지
                lower_blue = np.array([100, 150, 0])  # 파란색 범위 설정
                upper_blue = np.array([140, 255, 255])

                blue_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
                blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # 파란색이 감지되면 QR 코드 확인을 시도
                if blue_contours and not rotation_sequence_active:
                    print("Blue area detected, stopping to check QR code.")
                    motor_running = False  # 파란색 감지 시 정지

                    # QR 코드 감지
                    decoded_objects = pyzbar.decode(qr_frame)
                    if decoded_objects:
                        for obj in decoded_objects:
                            detected_data = obj.data.decode('utf-8')
                            print(f"QR 코드 데이터: {detected_data}")

                            # QR 코드 데이터가 원하는 것과 일치하는 경우
                            if detected_data == qr_data:
                                print("QR 코드 일치: 직진 및 회전 시퀀스 시작")
                                rotation_sequence_active = True  # 회전 시퀀스 시작

                                # 1초간 직진 (단일 명령으로 유지)
                                self.myagv.go_ahead(5, 1.3)
                                time.sleep(0.5)  # 직진 시간 동안 유지

                                # 3.5초 동안 단일 호출로 회전
                                self.myagv.clockwise_rotation(5, 4)
                                time.sleep(0.5)  # 충분한 시간 동안 회전 유지

                                # 회전 시퀀스 후 이동 재개 설정
                                motor_running = True  # 회전 시퀀스 후 이동 재개
                                qr_data = None  # QR 데이터 초기화
                                detected_data = None  # QR 감지된 데이터 초기화
                                rotation_sequence_active = False  # 회전 시퀀스 완료
                            else:
                                # QR 코드가 일치하지 않으면 직진 재개
                                print("QR 코드가 일치하지 않음: 계속 직진.")
                                motor_running = True
                    else:
                        # QR 코드가 감지되지 않으면 직진 재개
                        print("QR 코드가 감지되지 않음: 계속 직진.")
                        motor_running = True
                elif not rotation_sequence_active:
                    # 노란색 라인 감지 및 오프셋 계산
                    lower_yellow = np.array([22, 70, 97])
                    upper_yellow = np.array([42, 236, 241])

                    yellow_mask = cv2.inRange(img_hsv, lower_yellow, upper_yellow)
                    yellow_contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                    if yellow_contours:
                        max_contour = max(yellow_contours, key=cv2.contourArea)
                        if cv2.contourArea(max_contour) > 1000:
                            M = cv2.moments(max_contour)
                            if M["m00"] != 0:
                                cx = int(M["m10"] / M["m00"])
                                with offset_lock:
                                    offset = cx - width // 2
                                print(f"Calculated offset: {offset}")
                    else:
                        print("No yellow line detected.")
                        motor_running = False
                        offset = -900

        self.vid.release()

class AgvControlThread(Thread):
    def __init__(self, myagv):
        Thread.__init__(self)
        self.myagv = myagv
    
    def run(self):
        global offset, motor_running, udp_run, qr_data, detected_data

        while udp_run:
            with offset_lock:
                current_offset = offset
                if motor_running and 800 > current_offset > 30:
                    print(f"Object is {current_offset} pixels to the right. Moving AGV left.")
                    self.myagv.clockwise_rotation(5, 0.2)
                elif motor_running and -800 < current_offset < -30:
                    print(f"Object is {-current_offset} pixels to the left. Moving AGV right.")
                    self.myagv.counterclockwise_rotation(5, 0.2)
                elif motor_running and -30 <= current_offset <= 30:
                    print('Object is centered. Moving AGV forward.')
                    self.myagv._mesg(128+8, 128, 128)
                else:
                    self.myagv.stop()
            time.sleep(0.2)

def main():
    global motor_running, udp_run, qr_data

    # MyAGV 객체 생성
    myagv = MyAgv('/dev/ttyAMA2', 115200)

    # 사용자 입력을 통해 시작 시 QR 코드 데이터를 설정
    while True:
        user_input = input("Enter 1, 2, or 3 to start the AGV with the corresponding QR data (1-ccw, 2-ccw, 3-ccw): ")
        if user_input == '1':
            qr_data = '1-ccw'
            break
        elif user_input == '2':
            qr_data = '2-ccw'
            break
        elif user_input == '3':
            qr_data = '3-ccw'
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

    print(f"Starting AGV with QR code data: {qr_data}")
    motor_running = True

    # 영상 처리 스레드 시작
    video_thread = VideoProcessingThread(400, myagv)
    video_thread.daemon = True
    video_thread.start()

    # AGV 제어 스레드 시작
    agv_thread = AgvControlThread(myagv)
    agv_thread.daemon = True
    agv_thread.start()

    # 메인 루프 - 종료 명령 대기
    try:
        while True:
            if not udp_run:
                break
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Exiting program...")
        udp_run = False
        myagv.stop()

if __name__ == '__main__':
    main()
