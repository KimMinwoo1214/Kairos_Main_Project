from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 도서 데이터
books = [
    {"id": 1, "title": "로봇 공학 입문"},
    {"id": 2, "title": "인공지능 기초"},
    {"id": 3, "title": "파이썬 프로그래밍"},
    {"id": 4, "title": "머신러닝의 이해"},
    {"id": 5, "title": "데이터 분석 실습"},
    {"id": 6, "title": "알고리즘 문제 해결"},
    {"id": 7, "title": "네트워크 보안"},
    {"id": 8, "title": "웹 개발 입문"},
    {"id": 9, "title": "JavaScript 마스터"},
    {"id": 10, "title": "HTML과 CSS 디자인"},
    {"id": 11, "title": "클라우드 컴퓨팅"},
    {"id": 12, "title": "데이터베이스 기초"},
    {"id": 13, "title": "운영체제의 이해"},
    {"id": 14, "title": "리눅스 활용법"},
    {"id": 15, "title": "React.js 실전"},
    {"id": 16, "title": "Node.js 활용하기"},
    {"id": 17, "title": "C++로 배우는 프로그래밍"},
    {"id": 18, "title": "컴퓨터 비전 입문"},
    {"id": 19, "title": "딥러닝 제대로 배우기"},
    {"id": 20, "title": "AI와 인간의 미래"}
]

@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('q', '').lower()
    filtered_books = [book for book in books if query in book['title'].lower()]
    return jsonify(filtered_books if filtered_books else books)

@app.route('/rent', methods=['POST'])
def rent_book():
    data = request.json
    book_id = data.get("bookId")
    if book_id:
        print(f"책 ID {book_id} 대여 요청 처리 중...")
        return jsonify({"message": f"책 ID {book_id} 대여 요청을 받았습니다."})
    return jsonify({"message": "책 ID가 누락되었습니다."}), 400

if __name__ == '__main__':
    app.run(debug=True)
