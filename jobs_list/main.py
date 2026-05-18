from flask import Flask, render_template
from data.db_session import global_init, create_session
from data.models import Job

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mars-mission-secret'

global_init('mars.db')

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/jobs')
def list_jobs():
    db_sess = create_session()
    jobs = db_sess.query(Job).all()
    db_sess.close()
    return render_template('jobs.html', jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True)