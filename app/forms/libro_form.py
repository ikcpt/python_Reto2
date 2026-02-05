from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length

# 1. Formulario para Crear y Editar Libros
class LibroForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(), Length(max=200)])
    autor = StringField('Autor', validators=[DataRequired(), Length(max=100)])
    genero = StringField('Género', validators=[DataRequired(), Length(max=50)])
    anio = IntegerField('Año', validators=[DataRequired()])
    resumen = TextAreaField('Resumen')
    submit = SubmitField('Guardar Libro')

# 2. Formulario para Prestar Libros
class PrestarLibroForm(FlaskForm):
    socio_id = SelectField('Seleccionar Socio', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Confirmar Préstamo')

# 3. Formulario para Buscar y Filtrar (NUEVO)
class BusquedaLibroForm(FlaskForm):
    titulo = StringField('Buscar por título')
    solo_disponibles = BooleanField('Ver solo disponibles')
    submit = SubmitField('Buscar')