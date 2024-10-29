﻿#ifndef _SMS_STS_H
#define _SMS_STS_H

// 내장 메모리 표 정의
// -------EPROM(읽기 전용)--------
#define SMS_STS_MODEL_L 3
#define SMS_STS_MODEL_H 4

// -------EPROM(읽기/쓰기)--------
#define SMS_STS_ID 5
#define SMS_STS_BAUD_RATE 6
#define SMS_STS_MIN_ANGLE_LIMIT_L 9
#define SMS_STS_MIN_ANGLE_LIMIT_H 10
#define SMS_STS_MAX_ANGLE_LIMIT_L 11
#define SMS_STS_MAX_ANGLE_LIMIT_H 12
#define SMS_STS_CW_DEAD 26
#define SMS_STS_CCW_DEAD 27
#define SMS_STS_OFS_L 31
#define SMS_STS_OFS_H 32
#define SMS_STS_MODE 33

// -------SRAM(읽기/쓰기)--------
#define SMS_STS_TORQUE_ENABLE 40
#define SMS_STS_ACC 41
#define SMS_STS_GOAL_POSITION_L 42
#define SMS_STS_GOAL_POSITION_H 43
#define SMS_STS_GOAL_TIME_L 44
#define SMS_STS_GOAL_TIME_H 45
#define SMS_STS_GOAL_SPEED_L 46
#define SMS_STS_GOAL_SPEED_H 47
#define SMS_STS_TORQUE_LIMIT_L 48
#define SMS_STS_TORQUE_LIMIT_H 49
#define SMS_STS_LOCK 55

// -------SRAM(읽기 전용)--------
#define SMS_STS_PRESENT_POSITION_L 56
#define SMS_STS_PRESENT_POSITION_H 57
#define SMS_STS_PRESENT_SPEED_L 58
#define SMS_STS_PRESENT_SPEED_H 59
#define SMS_STS_PRESENT_LOAD_L 60
#define SMS_STS_PRESENT_LOAD_H 61
#define SMS_STS_PRESENT_VOLTAGE 62
#define SMS_STS_PRESENT_TEMPERATURE 63
#define SMS_STS_MOVING 66
#define SMS_STS_PRESENT_CURRENT_L 69
#define SMS_STS_PRESENT_CURRENT_H 70

#include "SCSerial.h"

class SMS_STS : public SCSerial
{
public:
    SMS_STS();
    SMS_STS(u8 End);
    SMS_STS(u8 End, u8 Level);
    
    virtual int WritePosEx(u8 ID, s16 Position, u16 Speed, u8 ACC = 0); // 일반적인 서보 모터 위치 쓰기 명령
    virtual int RegWritePosEx(u8 ID, s16 Position, u16 Speed, u8 ACC = 0); // 비동기적으로 서보 모터 위치 쓰기 명령
    virtual void SyncWritePosEx(u8 ID[], u8 IDN, s16 Position[], u16 Speed[], u8 ACC[]); // 여러 서보 모터 위치 동기 쓰기 명령
    virtual int WheelMode(u8 ID); // 일정 속도 모드
    virtual int WriteSpe(u8 ID, s16 Speed, u8 ACC = 0); // 일정 속도 모드 제어 명령
    virtual int EnableTorque(u8 ID, u8 Enable); // 토크 제어 명령
    virtual int unLockEprom(u8 ID); // EEPROM 잠금 해제
    virtual int LockEprom(u8 ID); // EEPROM 잠금
    virtual int CalibrationOfs(u8 ID); // 캘리브레이션
    virtual int FeedBack(int ID); // 서보 모터 정보 피드백
    virtual int ReadPos(int ID); // 위치 읽기
    virtual int ReadSpeed(int ID); // 속도 읽기
    virtual int ReadLoad(int ID); // 모터에 출력되는 전압 비율 읽기(0~1000)
    virtual int ReadVoltage(int ID); // 전압 읽기
    virtual int ReadTemper(int ID); // 온도 읽기
    virtual int ReadMove(int ID); // 이동 상태 읽기
    virtual int ReadCurrent(int ID); // 전류 읽기
    virtual int ReadMode(int ID);

    int CalibrationOfs(u8 ID); // 캘리브레이션 오프셋 설정 함수
    int ReadPos(int ID); // 위치 읽기 함수

private:
    u8 Mem[SMS_STS_PRESENT_CURRENT_H - SMS_STS_PRESENT_POSITION_L + 1];
    int calibrationOffset; // 캘리브레이션 오프셋 변수 추가
};

#endif
