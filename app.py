from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # '/' 메인화면, 127.0.0.1
def hello():
    return "Hello World!"

@app.route('/kb') # '/' 서브화면, 127.0.0.1/kb
def kb():
    return "kbbaseball!"

@app.route('/face') # '/' 서브화면, 127.0.0.1/face
def face():
    return render_template('face.html')

if __name__ == '__main__':
    app.run(port=80) # flask default port = 5000, web default 80번 변경
#    app.run(host='0.0.0.0', port=80) # 루프백이 아닌 외부와 주소 연결 설정, 다 열어준다.

# git remote add origin https://github.com/urgoodfriend-py/web.git
# git branch -M main
# git push -u origin main