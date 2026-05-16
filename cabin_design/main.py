from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <h1>Оформление кают</h1>
    <p>Примеры URL:</p>
    <ul>
        <li><a href="/table/male/25">/table/male/25</a> - мужчина, 25 лет</li>
        <li><a href="/table/female/18">/table/female/18</a> - девушка, 18 лет</li>
        <li><a href="/table/male/45">/table/male/45</a> - мужчина, 45 лет</li>
        <li><a href="/table/female/30">/table/female/30</a> - девушка, 30 лет</li>
    </ul>
    '''


@app.route('/table/<gender>/<int:age>')
def table(gender, age):
    if gender.lower() == 'male':
        wall_color = '#FF4500'
        color_name = 'Оранжево-красный'
    elif gender.lower() == 'female':
        wall_color = '#6495ED'
        color_name = 'Голубой'
    else:
        wall_color = '#CCCCCC'
        color_name = 'Серый'

    if age < 21:
        alien_image = 'alien_child.svg'
        alien_type = 'Марсианин-ребёнок'
    else:
        alien_image = 'alien_adult.svg'
        alien_type = 'Взрослый марсианин'

    return render_template('table.html',
                           gender=gender,
                           age=age,
                           wall_color=wall_color,
                           color_name=color_name,
                           alien_image=alien_image,
                           alien_type=alien_type)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
