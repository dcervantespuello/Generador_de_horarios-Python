from flask import Flask, render_template
from py.funciones import dataframe_limpio, indexar_columnas

app = Flask(__name__)
df = dataframe_limpio()
df2 = indexar_columnas(df)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('test.html', df2=df2)


@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
