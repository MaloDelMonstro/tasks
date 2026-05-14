from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():
    return '''
    <form method="POST" action="/answer" style="font-family:sans-serif; padding:20px; max-width:400px;">
        <input name="title" placeholder="title"><br><br>
        <input name="surname" placeholder="surname"><br><br>
        <input name="name" placeholder="name"><br><br>
        <input name="education" placeholder="education"><br><br>
        <input name="profession" placeholder="profession"><br><br>
        <input name="sex" placeholder="sex"><br><br>
        <input name="motivation" placeholder="motivation"><br><br>
        <input name="ready" placeholder="ready"><br><br>
        <button type="submit">Отправить анкету</button>
    </form>
    '''

@app.route('/answer', methods=['POST'])
def answer():
    data = {
        'title': request.form.get('title'),
        'surname': request.form.get('surname'),
        'name': request.form.get('name'),
        'education': request.form.get('education'),
        'profession': request.form.get('profession'),
        'sex': request.form.get('sex'),
        'motivation': request.form.get('motivation'),
        'ready': request.form.get('ready')
    }
    session['anketa'] = data
    return redirect(url_for('auto_answer'))

@app.route('/auto_answer')
def auto_answer():
    data = session.get('anketa', {})
    return render_template('auto_answer.html', **data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)