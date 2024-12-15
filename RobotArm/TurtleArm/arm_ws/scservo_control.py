import serial

PORT = '/dev/ttyAMA1'  # Raspberry Pi에서 USB-Serial 어댑터 포트
BAUD_RATE = 1000000    # 서보 모터의 Baud Rate

def calculate_checksum(data):
    """Checksum 계산"""
    return (~(sum(data) % 256)) & 0xFF

try:
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    print(f"Serial port {PORT} opened successfully!")

    # 서보 ID와 목표 위치 설정
    servo_id = 6  # 실제 서보 ID로 변경
    position = 1700  # 이동 목표 위치
    speed = 500  # 이동 속도
    torque = 1023  # 최대 토크

    # 데이터 생성
    position_l = position & 0xFF
    position_h = (position >> 8) & 0xFF
    speed_l = speed & 0xFF
    speed_h = (speed >> 8) & 0xFF
    torque_l = torque & 0xFF
    torque_h = (torque >> 8) & 0xFF

    # 패킷 생성
    packet = [
        0xFF, 0xFF,  # Header
        servo_id,    # ID
        7,           # Length (Command + Parameters + Checksum)
        0x03,        # Command (Write Position)
        position_l, position_h, speed_l, speed_h, torque_l, torque_h
    ]
    checksum = calculate_checksum(packet[2:])  # Checksum 계산
    packet.append(checksum)

    # 패킷 송신
    ser.write(bytearray(packet))
    print(f"Packet sent: {packet}")

except Exception as e:
    print(f"Error: {e}")
