from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    position = db.Column(db.String(255))
    speciality = db.Column(db.String(255))
    address = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
    city_from = db.Column(db.String(255))


class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    team_leader = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    job = db.Column(db.String(255), nullable=False)
    work_size = db.Column(db.Integer, nullable=False)
    collaborators = db.Column(db.String(255))
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_finished = db.Column(db.Boolean, default=False)

    leader = db.relationship('User', foreign_keys=[team_leader])
