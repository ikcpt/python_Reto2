from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class PrestarLibroForm(FlaskForm):
    socio_id = SelectField('Seleccionar Socio', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Confirmar Préstamo')

    def __init__(self, *args, **kwargs):
        super(PrestarLibroForm, self).__init__(*args, **kwargs)
        from app.services.socio_service import SocioService
        socios = SocioService.obtener_todos()
        self.socio_id.choices = [(s.id, f"{s.nombre} - {s.email}") for s in socios]