#include <SCServo.h>

// SCSCL 객체 생성
SMS_STS sts;

void setup() {
  Serial.begin(1000000);  // 서보와 통신 (1Mbps)
  sts.pSerial = &Serial;  // Serial을 SCServo 객체에 할당
  delay(500);  // 통신 안정화 대기
}

void loop() {
  if (Serial.available() > 0) {
    // 시리얼로부터 각도 값을 읽어온다
    String input = Serial.readStringUntil('\n'); // 한 줄 읽기
    int angle0, angle1, angle2, angle3;

    // 입력된 문자열을 ,로 분리하여 각도 값으로 변환
    int comma1 = input.indexOf(',');
    int comma2 = input.indexOf(',', comma1 + 1);
    int comma3 = input.indexOf(',', comma2 + 1);
    
    if (comma1 != -1 && comma2 != -1) {
      angle0 = input.substring(0, comma1).toInt();
      angle1 = input.substring(comma1 + 1, comma2).toInt();
      angle2 = input.substring(comma2 + 1, comma3).toInt();
      angle3 = input.substring(comma3 + 1).toInt();

      // 각도 값을 사용하여 서보 모터 움직임 예약
      sts.RegWritePosEx(0, angle0, 500, 0);  // 서보1에 각도값 전송
      sts.RegWritePosEx(1, angle1, 500, 0);  // 서보1에 각도값 전송
      sts.RegWritePosEx(2, 4227 - angle1, 500, 0);  // 서보2에 반대각도값 전송
      sts.RegWritePosEx(3, angle2, 500, 0);  // 서보3에 각도값 전송
      sts.RegWritePosEx(4, angle3, 500, 0);  // 서보4에 각도값 전송
      delay(1000);
      sts.RegWriteAction();  // 예약된 명령을 동시 실행
      delay(1000);  // 움직임 완료 대기
    }
  }

  Serial.flush();  // 버퍼 비우기
  delay(1000);  // 읽기 주기 설정
}
