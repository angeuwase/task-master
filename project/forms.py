from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('login')

class TaskForm(FlaskForm):
    content = TextField('Add a new task', validators=[DataRequired()])
    submit = SubmitField('submit')

class UpdateForm(FlaskForm):
    content = TextField('Update task', validators=[DataRequired()])
    submit = SubmitField('submit')

