from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from CC_Flask import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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