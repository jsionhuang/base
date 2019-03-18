from flask import Flask,render_template
from flask import Blueprint



app01 = Blueprint('app01',__name__)


app = Flask(__name__)
app.register_blueprint(app01,url_prefix='/app01')

@app.route('/')
def hhhh():
    return 'hhhh'

@app.route('/index',methods=['POST','GET'])
def index():
    return render_template('index.html')


@app01.route('/test')
def test():
    return 'hello flask'

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)