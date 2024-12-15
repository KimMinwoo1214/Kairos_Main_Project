import serial
import time

PORT = '/dev/ttyAMA1'  # Raspberry Pi에서 사용하는 시리얼 포트
BAUD_RATE = 1000000    # 서보 모터의 Baud Rate

def calculate_checksum(data):
    """Checksum 계산"""
    return (~(sum(data) % 512)) & 0xFF

def write_servo_position(ser, servo_id, position, speed=100):
    """
    서보의 목표 위치와 속도를 설정하는 함수.
    ser: Serial 포트 객체
    servo_id: 설정할 서보의 ID
    position: 목표 위치 (0~1023)
    speed: 모터 속도 (기본값: 100)
    """
    try:
        # Goal Position 명령 패킷 생성
        packet = [
            0xFF, 0xFF,             # Header
            servo_id,               # 서보 ID
            0x07,                   # Length (Instruction + Parameters + Checksum)
            0x03,                   # Instruction: Write Data
            0x2A,                   # Start Address (Goal Position address)
            position & 0xFF,        # Position LSB (Low Byte)
            (position >> 8) & 0xFF, # Position MSB (High Byte)
            speed & 0xFF,           # Speed LSB (Low Byte)
            (speed >> 8) & 0xFF     # Speed MSB (High Byte) 
        ]
        checksum = calculate_checksum(packet[2:])  # Checksum 계산
        packet.append(checksum)

        # 패킷 전송
        ser.write(bytearray(packet))
        print(f"Write packet sent: {packet}")

    except Exception as e:
        print(f"Error: {e}")


# 메인 실행
try:
    # Serial 포트 열기
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    print(f"Serial port {PORT} opened successfully!")

    # 서보 ID와 목표 위치 설정
    servo_id = 0       # 설정할 서보 ID
    target_position = 1000  # 목표 위치 (중앙)
    speed = 100
            # 모터 속도 설정

    # 서보 위치 설정 함수 호출
    #write_servo_position(ser, servo_id, target_position, speed)
    time.sleep(5)
    write_servo_position(ser, 0, target_position, speed)
    write_servo_position(ser, 1, target_position, speed)
    #write_servo_position(ser, 2, target_position, speed)
    # write_servo_position(ser, 2, 3837-target_position, speed)
    #write_servo_position(ser, 4, target_position+150, speed)
    # time.sleep(5)
    # write_servo_position(ser, 1, 2047, speed)
    # write_servo_position(ser, 3, target_position - 150, speed)
    # write_servo_position(ser, 4, target_position, speed)

except Exception as e:
    print(f"Error: {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
