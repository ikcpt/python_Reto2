from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

class BusquedaLibroForm(FlaskForm):
    titulo = StringField('Buscar por título')
    solo_disponibles = BooleanField('Ver solo disponibles')
    submit = SubmitField('Buscar')