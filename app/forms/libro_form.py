from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class LibroForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(), Length(max=200)])
    autor = StringField('Autor', validators=[DataRequired(), Length(max=100)])
    genero = StringField('Género', validators=[DataRequired(), Length(max=50)])
    anio = IntegerField('Año', validators=[DataRequired()])
    resumen = TextAreaField('Resumen')
    submit = SubmitField('Guardar Libro')