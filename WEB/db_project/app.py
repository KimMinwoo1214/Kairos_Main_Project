from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# 도서 목록을 가져오는 함수
def get_books(search=None):
    conn = sqlite3.connect('db_project/books.db')
    cursor = conn.cursor()
     # 검색어가 있으면 LIKE 쿼리로 책 제목을 필터링
    if search:
        cursor.execute('SELECT id, title, rent FROM books WHERE title LIKE ?', ('%' + search + '%',))
    else:
        cursor.execute('SELECT id, title, rent FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

# 메인 페이지
@app.route('/')
def index():
    search = request.args.get('search')  # 검색어를 GET 파라미터로 받음
    books = get_books(search)
    return render_template('index.html', books=books)

# 대여/반납 처리
@app.route('/rent_book/<int:book_id>', methods=['POST'])
def rent_book(book_id):
    try:
        conn = sqlite3.connect('db_project/books.db')
        cursor = conn.cursor()

        # 현재 상태 가져오기
        cursor.execute('SELECT rent FROM books WHERE id = ?', (book_id,))
        rent_status = cursor.fetchone()[0]
        print(f"현재 rent 상태: {rent_status}")  # 로그 추가

        # 대여 상태 변경 (반납 <=> 대여)
        if rent_status == 0:
            cursor.execute('UPDATE books SET rent = 1 WHERE id = ?', (book_id,))
            conn.commit()
            conn.close()
            print(f"렌트 상태 변경: 책 ID {book_id} -> 대여됨")  # 로그 추가
            return jsonify({"success": True, "rent": 1})  # 대여 상태로 변경
        else:
            cursor.execute('UPDATE books SET rent = 0 WHERE id = ?', (book_id,))
            conn.commit()
            conn.close()
            print(f"렌트 상태 변경: 책 ID {book_id} -> 반납됨")  # 로그 추가
            return jsonify({"success": True, "rent": 0})  # 반납 상태로 변경

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": "처리 중 오류 발생"})

if __name__ == '__main__':
    app.run(host="172.30.1.8", port=5000, debug=True)
