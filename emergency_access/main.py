from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<a href="/emergency">Аварийный доступ к системам корабля</a>'


@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    if request.method == 'POST':
        astronaut_id = request.form.get('astronaut_id')
        astronaut_pass = request.form.get('astronaut_pass')
        captain_id = request.form.get('captain_id')
        captain_token = request.form.get('captain_token')

        if astronaut_id and astronaut_pass and captain_id and captain_token:
            return f'''
            <h1>Доступ разрешён!</h1>
            <p>Астронавт: {astronaut_id}</p>
            <p>Капитан: {captain_id}</p>
            <p>Системы корабля разблокированы.</p>
            <a href="/emergency">Назад</a>
            '''

    return render_template('emergency.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
