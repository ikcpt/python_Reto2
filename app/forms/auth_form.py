from flask_wtf import FlaskForm
# Fíjate aquí: he añadido EmailField al final
from wtforms import StringField, PasswordField, SubmitField, EmailField
# Fíjate aquí: he añadido Email al final
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class RegistroForm(FlaskForm):
    username = StringField('Usuario', validators=[
        DataRequired(), 
        Length(min=4, max=25)
    ])
    
    # Campo de Email
    email = EmailField('Email', validators=[DataRequired(), Email()]) 
    
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrar Admin')