import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('db_project/books.db')
cursor = conn.cursor()

# 테이블 생성 (이미 존재하면 건너뛰기)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        status INTEGER defalt 0
    )
''')

# 예시 도서 추가
books = [
    ('로봇 공학 입문',),
    ('인공지능 기초',),
    ('파이썬 프로그래밍',),
    ('자바 기초',),
    ('웹 개발 입문',),
    ('데이터 과학 입문',),
    ('머신러닝 기초',),
    ('딥러닝 입문',),
    ('C++ 프로그래밍',),
    ('시스템 프로그래밍',),
    ('네트워크 기초',),
    ('클라우드 컴퓨팅',),
    ('모바일 앱 개발',),
    ('게임 개발 기초',),
    ('블록체인 기초',),
    ('인공지능 기초 2',),
    ('자연어 처리 입문',),
    ('자바스크립트 프로그래밍',),
    ('HTML/CSS 기초',),
    ('웹 디자인 입문',)
]

# 데이터 삽입
cursor.executemany('''
    INSERT INTO books (title) VALUES (?)
''', books)

# 변경사항 저장
conn.commit()

# 연결 종료
conn.close()
