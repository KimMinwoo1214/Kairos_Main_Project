import cv2
from ultralytics import YOLO
import time

# YOLOv8 모델 로드
model = YOLO(r'/home/kmw/best.pt')  # 실제 경로로 수정하세요.

# 비디오 파일 열기 (0은 웹캠, 비디오 파일 경로를 입력할 수도 있습니다)
video_source = 0  # 웹캠을 사용할 경우
cap = cv2.VideoCapture(video_source)

# 클래스 이름과 임계값 설정
confidence_threshold = 0.75  # 75% 확률
duration = 2  # 2초

# 시간 체크를 위한 변수
start_time_frog_dog = None
start_time_cat = None

while True:
    ret, frame = cap.read()
    if not ret:
        print("비디오에서 프레임을 읽을 수 없습니다.")
        break

    # 객체 탐지 수행
    results = model(frame)

    # 결과를 이미지에 표시
    annotated_frame = results[0].plot()  # 첫 번째 결과를 선택

    # 클래스 탐지 및 성공 조건 체크
    detected_frog_or_dog = False
    detected_cat = False

    for result in results:
        for box in result.boxes:
            confidence = box.conf
            class_name = model.names[int(box.cls)]

            # 신뢰도 체크
            if confidence >= confidence_threshold:
                if class_name in ['yellow', 'blue']:
                    detected_frog_or_dog = True
                    if start_time_frog_dog is None:
                        start_time_frog_dog = time.time()  # 타이머 시작
                    elif time.time() - start_time_frog_dog >= duration:
                        print("통과")
                        cap.release()
                        cv2.destroyAllWindows()
                        exit()  # 영상 종료
                elif class_name == 'cat':
                    detected_cat = True
                    if start_time_cat is None:
                        start_time_cat = time.time()  # 타이머 시작
                    elif time.time() - start_time_cat >= duration:
                        print("출입 불가")
                        cap.release()
                        cv2.destroyAllWindows()
                        exit()  # 영상 종료
            else:
                if class_name in ['yellow']:
                    start_time_frog_dog = None  # 조건이 충족되지 않으면 타이머 초기화
                elif class_name == 'blue':
                    start_time_cat = None  # 조건이 충족되지 않으면 타이머 초기화

    # 탐지되지 않은 경우 타이머 초기화
    if not detected_frog_or_dog:
        start_time_frog_dog = None
    if not detected_cat:
        start_time_cat = None

    # 결과 프레임을 화면에 표시
    cv2.imshow("YOLOv8 Object Detection", annotated_frame)

    # 'q' 키를 눌러 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 캡처 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()
