from flask import Flask

# Flask는 우리가 지정하지 않으면 기본적으로 app.py를 시작점으로 인식해서 찾아나감
# Flask 패키지에 있는 클래스를 통해 어플리케이션의 입구를 만들어줌
app = Flask(__name__)

# 라우팅 주소를 만들때는 '/경로명'까지만 적어주기
@app.route('/')
def hello():
    return f'hello, {__name__}'

@app.route('/Nova')
def hello_Nova():
    return f'<b> hello, Nova Grace </b>'