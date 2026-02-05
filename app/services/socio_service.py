from app import db
from app.models.socio import Socio

class SocioService:
    @staticmethod
    def obtener_todos():
        return Socio.query.all()

    @staticmethod
    def obtener_por_id(id):
        return Socio.query.get_or_404(id)

    @staticmethod
    def crear_socio(datos_form):
        nuevo_socio = Socio(
            nombre=datos_form.nombre.data,
            email=datos_form.email.data
        )
        db.session.add(nuevo_socio)
        db.session.commit()
        return nuevo_socio

    @staticmethod
    def editar_socio(id, datos_form):
        socio = Socio.query.get_or_404(id)
        socio.nombre = datos_form.nombre.data
        socio.email = datos_form.email.data
        db.session.commit()
        return socio