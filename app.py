from flask import Flask, render_template, request
import nvapi

app = Flask(__name__)

@app.route('/') # '/' 메인화면, 127.0.0.1
def hello():
    return "Hello World!"

@app.route('/kb') # '/' 서브화면, 127.0.0.1/kb
def kb():
    return "kbbaseball!"

@app.route('/face', methods=['GET', 'POST']) # '/' 서브화면, 127.0.0.1/face
def face():
    if request.method == 'GET':
        return render_template('face.html')
    else:
        imgurl = request.form['imgurl']
        # 여기에 face()
        name = nvapi.judgment(imgurl)
        print(name)
        return '''
            <h1>{0}</h1>
            <img src='{1}'>
        '''.format(name, imgurl)

if __name__ == '__main__':
    app.run(port=80, debug=True) # flask default port = 5000, web default 80번 변경
#    app.run(host='0.0.0.0', port=80) # 루프백이 아닌 외부와 주소 연결 설정, 다 열어준다.

# git remote add origin https://github.com/urgoodfriend-py/web.git
# git branch -M main
# git push -u origin main

# git config --global user.email "urgoodfriend@naver.com"
# git config --global user.name "urgoodfriend-py"