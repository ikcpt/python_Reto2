from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email

class RegistroForm(FlaskForm):
    username = StringField('Usuario', validators=[
        DataRequired(), 
        Length(min=4, max=25)
    ])
    email = EmailField('Email', validators=[DataRequired(), Email()]) 
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrar Admin')