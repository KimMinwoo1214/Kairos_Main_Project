#include <SCServo.h>

// SCSCL 객체 생성
SMS_STS sts;
bool isCalibrated = false; // 캘리브레이션 여부를 확인하는 플래그

void setup() {
  Serial.begin(1000000);  // 서보와 통신 (1Mbps)
  sts.pSerial = &Serial;   // Serial을 SCServo 객체에 할당
  delay(500);
}

void loop() {
  // 최초 한 번만 캘리브레이션 수행
  if (!isCalibrated) {
    sts.CalibrationOfs(1); // ID 1 서보 캘리브레이션
    sts.CalibrationOfs(2); // ID 2 서보 캘리브레이션
    sts.CalibrationOfs(3); // ID 3 서보 캘리브레이션
    sts.CalibrationOfs(4); // ID 4 서보 캘리브레이션
    isCalibrated = true;   // 캘리브레이션 완료 표시
    delay(1000);           // 캘리브레이션 안정화를 위한 대기
  }

  if (Serial.available() > 0) {
    // 시리얼로부터 각도 값을 읽어온다
    String input = Serial.readStringUntil('\n'); // 한 줄 읽기
    int angle1, angle2, angle3;

    // 입력된 문자열을 ,로 분리하여 각도 값으로 변환
    int comma1 = input.indexOf(',');
    int comma2 = input.indexOf(',', comma1 + 1);

    if (comma1 != -1 && comma2 != -1) {
      angle1 = input.substring(0, comma1).toInt();
      angle2 = input.substring(comma1 + 1, comma2).toInt();
      angle3 = input.substring(comma2 + 1).toInt();

      // 각도 값을 사용하여 서보 모터 움직임 예약
      sts.RegWritePosEx(1, angle1 + 200, 1000, 0);
      sts.RegWritePosEx(2, 4295 - angle1, 1000, 0);
      sts.RegWritePosEx(3, angle2, 1000, 0);
      sts.RegWritePosEx(4, angle3 - 200, 1000, 0);
      delay(1000);
      sts.RegWriteAction(); // 예약된 명령을 동시 실행
      delay(1000); // 움직임 완료 대기
    }
  }
  Serial.flush();
}
