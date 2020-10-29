from flask import Flask
app = Flask(__name__)

@app.route('/') # '/' 메인화면, 127.0.0.1
def hello():
    return "Hello World!"

@app.route('/kb') # '/' 서브화면, 127.0.0.1/kb
def kb():
    return "kbbaseball!"

if __name__ == '__main__':
    app.run(port=80) # flask default port = 5000, web default 80번 변경

# git remote add origin https://github.com/urgoodfriend-py/web.git
# git branch -M main
# git push -u origin main