from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


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