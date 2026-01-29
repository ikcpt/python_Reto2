from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SocioForm(FlaskForm):
    nombre = StringField('Nombre y Apellidos', validators=[
        DataRequired(), 
        Length(min=3, max=100)
    ])
    
    email = EmailField('Correo Electrónico', validators=[
        DataRequired(), 
        Email(message="Introduce un email válido")
    ])
    
    submit = SubmitField('Guardar Socio')