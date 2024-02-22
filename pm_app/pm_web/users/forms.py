from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class Register_form(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=5, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class login_form(FlaskForm):
    email = StringField(label='Email', description='Your email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', description='Your password', validators=[])
    submit = SubmitField('Sign In')

class Project_form(FlaskForm):
    project_name = StringField('Input your project name', validators=[DataRequired(), Length(min=2, max=20)])
    description = StringField('Give a short description about your project', validators=[DataRequired(), Length(max=50)])
    create = SubmitField('Create')

class Task_form(FlaskForm):
    task = StringField('Add a new task', validators=[DataRequired()])
    priority = StringField("Chose either 'Low','Medium' or 'High'", validators=[DataRequired(), Length(max=7)])
    create = SubmitField('Create')

    # def validate_priority(self, priority):
    #     temp = ['LOW', 'MEDIUM', 'HIGH']
    #     # priority = priority.upper()
    #     if priority not in temp:
    #         raise ValidationError('Chose one of the provided priorities')