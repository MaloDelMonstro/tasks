from flask import Flask, render_template

app = Flask(__name__)

ENGINEERING_DATA = {
    'header': 'Инженерные тренажёры',
    'scheme': '/static/images/engineering_scheme.png',
    'program': [
        'Техническое обслуживание систем жизнеобеспечения',
        'Ремонт оборудования корабля',
        'Работа с 3D-принтером для печати запчастей',
        'Диагностика электрических систем',
        'Сборка и монтаж конструкций'
    ]
}

SCIENCE_DATA = {
    'header': 'Научные симуляторы',
    'scheme': '/static/images/science_scheme.png',
    'program': [
        'Проведение биологических экспериментов',
        'Геологические исследования Марса',
        'Атмосферные измерения',
        'Работа с лабораторным оборудованием',
        'Анализ образцов грунта'
    ]
}


def is_engineering_profession(profession):
    profession_lower = profession.lower()
    engineering_keywords = ['инженер', 'строитель', 'engineer', 'builder', 'technical', 'механик']

    for keyword in engineering_keywords:
        if keyword in profession_lower:
            return True
    return False


@app.route('/')
def index():
    return """
    <h1>Космическая миссия на Марс</h1>
    <p>Доступные специальности для тренировок:</p>
    <ul>
        <li><a href="/training/инженер-систем">Инженер систем</a></li>
        <li><a href="/training/строитель-базы">Строитель базы</a></li>
        <li><a href="/training/биолог">Биолог</a></li>
        <li><a href="/training/геолог">Геолог</a></li>
        <li><a href="/training/инженер-электрик">Инженер-электрик</a></li>
        <li><a href="/training/астроном">Астроном</a></li>
    </ul>
    """


@app.route('/training/<prof>')
def training(prof):
    if is_engineering_profession(prof):
        data = ENGINEERING_DATA
        is_eng = True
    else:
        data = SCIENCE_DATA
        is_eng = False

    context = {
        'profession': prof,
        'header_text': data['header'],
        'scheme_image': data['scheme'],
        'training_program': data['program'],
        'is_engineering': is_eng
    }

    return render_template('training.html', **context)


@app.errorhandler(404)
def page_not_found(e):
    return """
    <h1>404 - Страница не найдена</h1>
    <p>Вернитесь на <a href="/">главную страницу</a></p>
    """, 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
