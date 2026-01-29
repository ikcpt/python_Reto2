from app import db

class Socio(db.Model):
    __tablename__ = "socios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # Esto lo usaremos más adelante para saber qué libro tiene
    # pero de momento lo dejamos preparado.

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email
        }