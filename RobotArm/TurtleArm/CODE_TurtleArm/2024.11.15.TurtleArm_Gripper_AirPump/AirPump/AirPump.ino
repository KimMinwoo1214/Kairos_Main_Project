int motorPin = 9;  // 모터 제어 핀 설정
int solePin = 10;  // 모터 제어 핀 설정

void setup() {
  Serial.begin(9600);  // 시리얼 통신 시작
  pinMode(motorPin, OUTPUT);  // 모터 핀을 출력 모드로 설정
  pinMode(solePin, OUTPUT);  // 모터 핀을 출력 모드로 설정
  
  Serial.println("명령을 입력하세요:");
  Serial.println("'m on' - motorPin 활성화");
  Serial.println("'m off' - motorPin 비활성화");
  Serial.println("'s on' - solePin 활성화");
  Serial.println("'s off' - solePin 비활성화");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');  // 시리얼에서 명령 읽기
    command.trim();  // 공백 제거
    
    if (command == "m on") {
      digitalWrite(motorPin, HIGH);
      Serial.println("motorPin 활성화");
    } else if (command == "m off") {
      digitalWrite(motorPin, LOW);
      Serial.println("motorPin 비활성화");
    } else if (command == "s on") {
      digitalWrite(solePin, HIGH);
      Serial.println("solePin 활성화");
    } else if (command == "s off") {
      digitalWrite(solePin, LOW);
      Serial.println("solePin 비활성화");
    } else {
      Serial.println("알 수 없는 명령입니다. 다시 입력하세요.");
    }
  }
}
