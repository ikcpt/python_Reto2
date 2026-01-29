from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange
from wtforms import SelectField

class LibroForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(), Length(max=200)])
    autor = StringField('Autor', validators=[DataRequired(), Length(max=100)])
    genero = StringField('Género', validators=[DataRequired(), Length(max=50)])
    
    anio = IntegerField('Año de Publicación', validators=[
        DataRequired(),
        NumberRange(min=1000, max=2025, message="Introduce un año válido")
    ])

    resumen = TextAreaField('Resumen (Opcional)')
    submit = SubmitField('Guardar Libro')

class PrestarLibroForm(FlaskForm):
    socio_id = SelectField('Seleccionar Socio', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Confirmar Préstamo')