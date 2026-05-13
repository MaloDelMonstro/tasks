import webbrowser

from flask import Flask, render_template

app = Flask(__name__)

PROFESSIONS = [
    "Командир корабля",
    "Бортинженер",
    "Научный сотрудник",
    "Врач",
    "Пилот спускаемого аппарата"
]


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    return render_template('list_prof.html',
                           professions=PROFESSIONS,
                           list_type=list_type)


if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:8080/list_prof/ol")
    app.run(debug=True, host='0.0.0.0', port=8080)
