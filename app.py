from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # 개발용 서버 실행 (배포 시에는 gunicorn 등 WSGI 서버 사용을 권장합니다)
    app.run(host="0.0.0.0", port=5000, debug=True)
