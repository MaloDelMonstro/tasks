from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<a href="/distribution">Распределение по каютам</a>'


@app.route('/distribution')
def distribution():
    astronauts = [
        'Ридли Скотт',
        'Энди Уир',
        'Марк Уотни',
        'Венката Капур',
        'Тедди Сандерс',
        'Шон Бин'
    ]

    return render_template('distribution.html', astronauts=astronauts)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
