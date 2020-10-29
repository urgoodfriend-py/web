from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()

# git remote add origin https://github.com/urgoodfriend-py/web.git
# git branch -M main
# git push -u origin main