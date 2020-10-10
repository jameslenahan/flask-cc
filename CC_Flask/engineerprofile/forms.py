from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from CC_Flask.models import User


class EngineerprofileForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = TextAreaField('Lastname', validators=[DataRequired()])
    uscitizen = StringField('Uscitizen', validators=[DataRequired()])
    github = StringField('Github', validators=[DataRequired()])
    linkedin = StringField('Linkedin', validators=[DataRequired()])
    personalsite = StringField('Personalsite', validators=[DataRequired()])
    reason = StringField('Reason', validators=[DataRequired()])
    experienceyrs = StringField('Experienceyrs', validators=[DataRequired()])
    languages = StringField('Languages', validators=[DataRequired()])
    interest = StringField('Interest', validators=[DataRequired()])
    blurb = StringField('Blurb', validators=[DataRequired()])

    submit = SubmitField('Engineerprofile')

class UpdateEngineerForm(FlaskForm):
    firstname = StringField('Firstname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Lastname',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Update')
