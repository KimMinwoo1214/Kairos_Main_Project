#include <SCServo.h>

// SCSCL 객체 생성
SMS_STS sts;

void setup() {
  Serial.begin(1000000);  // 서보와 통신 (1Mbps)
  sts.pSerial = &Serial;   // Serial을 SCServo 객체에 할당
  delay(500);
}

void loop() {
  if (Serial.available() > 0) {
    // 시리얼로부터 속도 값을 읽어온다
    int speed = Serial.parseInt(); // 정수로 속도 값 읽기

    // 모터의 속도 설정
    sts.WriteSpe(3, speed, 0); // ID 1 모터 속도 설정 (ACC는 기본값 0)
  }
  Serial.flush();
}
