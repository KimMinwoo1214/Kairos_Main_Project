from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# 데이터베이스 연결 함수
def get_db_connection():
    conn = sqlite3.connect('books.db')  # 'books.db' 파일에 연결
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

# 도서 대여 함수
def rent_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE books SET rented = 1 WHERE id = ?', (book_id,))  # rented 값을 1로 설정
    conn.commit()
    conn.close()

# 기본 페이지: 도서 목록 페이지
@app.route('/')
def index():
    books = load_books_from_db()  # 도서 목록 가져오기
    return render_template('index.html', books=books)

# 대여 버튼 클릭 처리
@app.route('/rent/<int:book_id>', methods=['POST'])
def rent(book_id):
    rent_book(book_id)  # 도서 대여 처리
    return redirect(url_for('index'))  # 대여 후 다시 도서 목록 페이지로 리다이렉트

if __name__ == '__main__':
    app.run(debug=True)
