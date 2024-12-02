import serial


PORT = '/dev/ttyAMA1'  # Raspberry Pi에서 사용하는 시리얼 포트
BAUD_RATE = 1000000    # 서보 모터의 Baud Rate

def calculate_checksum(data):
    """Checksum 계산"""
    return (~(sum(data) % 256)) & 0xFF

def read_servo_position(ser, servo_id):
    """
    서보의 현재 위치를 읽어오는 함수.
    ser: Serial 포트 객체
    servo_id: 읽고자 하는 서보의 ID
    """
    try:
        # Read Position 명령 패킷 생성
        packet = [
            0xFF, 0xFF,             # Header
            servo_id,               # 서보 ID
            0x04,                   # Length (Instruction + Parameters + Checksum)
            0x02,                   # Instruction: Read Data
            0x38,                   # Start Address (Position data address)
            0x02                    # Length of data to read (2 bytes for Position)
        ]
        checksum = calculate_checksum(packet[2:])  # Checksum 계산
        packet.append(checksum)

        # 패킷 전송
        ser.write(bytearray(packet))
        print(f"Request packet sent: {packet}")

        # 응답 읽기
        response = ser.read(8)  # 응답 패킷 크기 (Header 2 + ID 1 + Length 1 + Data 2 + Checksum 1)
        if len(response) != 8:
            raise Exception("Invalid response length")

        # 응답 데이터 파싱
        if response[0] == 0xFF and response[1] == 0xFF and response[2] == servo_id:
            position_l = response[5]
            position_h = response[6]
            position = position_l + (position_h << 8)  # 2바이트 데이터를 결합
            checksum = response[7]
            
            # 응답 체크섬 검증
            if checksum == calculate_checksum(response[2:7]):
                print(f"Servo ID {servo_id} position: {position}")
                return position
            else:
                raise Exception("Checksum mismatch in response")
        else:
            raise Exception("Invalid response header or ID")
    except Exception as e:
        print(f"Error: {e}")
        return None


# 메인 실행
try:
    # Serial 포트 열기
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    print(f"Serial port {PORT} opened successfully!")

    # 서보 ID와 상태 읽기
    # 읽고자 하는 서보 ID
    position0 = read_servo_position(ser, 0)
    position1 = read_servo_position(ser, 1)
    position2 = read_servo_position(ser, 2)
    position3 = read_servo_position(ser, 3)
    position4 = read_servo_position(ser, 4)
    position5 = read_servo_position(ser, 5)


    # 포지션 출력
    if position is not None:
        print(f"Servo 0 Position: {position0}")
	#print(f"Servo 1 Position: {position1}")
	#print(f"Servo 2 Position: {position2}")
        #print(f"Servo 3 Position: {position3}")
	#print(f"Servo 4 Position: {position4}")
	#print(f"Servo 5 Position: {position5}")
    else:
        print("Failed to read position")

except Exception as e:
    print(f"Error: {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
