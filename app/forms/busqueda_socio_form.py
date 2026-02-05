from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class BusquedaSocioForm(FlaskForm):
    criterio = StringField('Buscar por nombre o email')
    submit = SubmitField('Buscar')