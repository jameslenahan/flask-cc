from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, current_app
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280bjf345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    concepts = db.relationship('Concept', backref='author', lazy=True)
    engineerprofile = db.relationship('Engineerprofile', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Concept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Concept('{self.title}', '{self.date_posted}')"

class Engineerprofile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    uscitizen = db.Column(db.String(100), nullable=False)
    github = db.Column(db.String(100), nullable=False)
    linkedin = db.Column(db.String(100), nullable=False)
    personalsite = db.Column(db.String(100), nullable=False)
    reason = db.Column(db.String(100), nullable=False)
    experienceyrs = db.Column(db.String(1000), nullable=False)
    languages = db.Column(db.String(1000), nullable=False)
    interest = db.Column(db.String(1000), nullable=False)
    blurb = db.Column(db.String(1000), nullable=False)


    def __repr__(self):
        return f"Engineerprofile('{self.firstname}', '{self.lastname}', '{self.uscitizen}', '{self.github}', '{self.linkedin}', '{self.personalsite}', '{self.reason}', '{self.experienceyrs}', '{self.languages}, '{self.interest}', '{self.blurb}')"