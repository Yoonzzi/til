import sqlite3
from flask import Flask
from flask import jsonify
app = Flask(__name__)

# 최상위 주소일때 밑에 있는 함수를 접속한다
@app.route("/")
def home():
    conn = sqlite3.connect("../db/test.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM items LIMIT 100")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    return jsonify(row)
    conn.close()

    #인코딩 문제 확인하기