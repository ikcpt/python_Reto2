from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# Formulario para Crear/Editar
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

# NUEVO: Formulario para Buscar
class BusquedaSocioForm(FlaskForm):
    criterio = StringField('Buscar por nombre o email')
    submit = SubmitField('Buscar')