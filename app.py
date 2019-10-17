from flask import Flask, render_template
from py.funciones import dataframe_limpio, indexar_columnas

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    df = dataframe_limpio()
    df = indexar_columnas(df)
    datos = df.to_numpy()

    return render_template('index.html',
                           columnas=df.columns.values,
                           datos=datos,
                           numero_datos=range(len(datos)),
                           numero_dato=range(5))


@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
