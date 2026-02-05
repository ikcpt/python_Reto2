from app import db
from app.models.usuario import Usuario

class AuthService:
    @staticmethod
    def obtener_por_username(username):
        return Usuario.query.filter_by(username=username).first()

    @staticmethod
    def crear_usuario(username, email, password):
        nuevo_usuario = Usuario(username=username, email=email)
        nuevo_usuario.set_password(password)
        
        db.session.add(nuevo_usuario)
        db.session.commit()
        return nuevo_usuario