import sqlite3

# 데이터베이스 연결 함수
def get_db_connection():
    conn = sqlite3.connect('db_project/books.db')  # 'books.db' 파일에 연결
    conn.row_factory = sqlite3.Row  # 결과를 딕셔너리 형식으로 반환
    return conn

# 도서 목록 조회 함수
def load_books_from_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')  # books 테이블에서 모든 데이터 조회
    books = cursor.fetchall()  # 모든 데이터 가져오기
    conn.close()
    return books

# 도서 목록 출력
books = load_books_from_db()
if books:  # 책이 존재하면 출력
    for book in books:
        print(f"ID: {book['id']}, 제목: {book['title']} 상태: {book['rent']}")
else:  # 책이 없을 경우 메시지 출력
    print("도서 목록이 비어 있습니다.")
