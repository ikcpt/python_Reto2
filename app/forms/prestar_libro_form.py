from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
# Importamos el servicio dentro del __init__ para evitar errores de "importación circular"
# si el servicio llegara a necesitar importar algo de aquí.

class PrestarLibroForm(FlaskForm):
    socio_id = SelectField('Seleccionar Socio', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Confirmar Préstamo')

    def __init__(self, *args, **kwargs):
        super(PrestarLibroForm, self).__init__(*args, **kwargs)
        
        # Importación local para evitar ciclos y usar la lógica de servicios
        from app.services.socio_service import SocioService
        
        # Obtenemos todos los socios usando el servicio
        socios = SocioService.obtener_todos()
        
        # Rellenamos el desplegable (Select) con los datos: (ID, Texto a mostrar)
        self.socio_id.choices = [(s.id, f"{s.nombre} - {s.email}") for s in socios]