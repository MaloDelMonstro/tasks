import json
import os
import random
from flask import Flask, render_template

app = Flask(__name__)


def load_crew_data():
    json_path = os.path.join('templates', 'crew.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


@app.route('/')
def index():
    return '''
    <h1>Система управления экипажем</h1>
    <p><a href="/member">Показать случайного члена экипажа</a></p>
    '''


@app.route('/member')
def member():
    crew_data = load_crew_data()

    random_member = random.choice(crew_data['crew'])

    return render_template('member.html', member=random_member)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
