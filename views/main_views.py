from flask import Blueprint

# Blueprint 클래스를 통해 임의의 객체 생성
# bp =  Blueprint('앱 내부에서 부를 별명', 전달되는 파일명, url_prefix="해당 블루프린트가 전달할 최상위경로")
bp =  Blueprint('main', __name__, url_prefix="/")

# 라우팅 주소를 만들때는 '/경로명'까지만 적어주기
@bp.route('/')
def hello():
    return f'hello, {__name__}'

@bp.route('/Nova')
def hello_Nova():
    return f'<b> hello, Nova Grace </b>'

