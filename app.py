from flask import Flask, render_template
from py.funciones import dataframe_limpio
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    df = dataframe_limpio()
    return render_template('index.html', df=df)


@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
