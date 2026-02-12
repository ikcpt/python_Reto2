from flask import Blueprint, jsonify
from app.models.libro import Libro
from app.models.socio import Socio

api_bp = Blueprint('api_rest', __name__, url_prefix='/api')

@api_bp.route('/libros', methods=['GET'])
def get_libros():
    libros = Libro.query.all()
    return jsonify([l.to_dict() for l in libros])

@api_bp.route('/librosdisponibles', methods=['GET'])
def get_libros_disponibles():
    libros = Libro.query.filter_by(disponible=True).all()
    return jsonify([l.to_dict() for l in libros])

@api_bp.route('/libros/buscar/<string:titulo>', methods=['GET'])
def buscar_libro(titulo):
    libros = Libro.query.filter(Libro.titulo.ilike(f'%{titulo}%')).all()
    return jsonify([l.to_dict() for l in libros])

@api_bp.route('/libros/socios/prestamos', methods=['GET'])
def get_socios_con_prestamos():
    socios = Socio.query.all()
    resultado = []
    
    for socio in socios:
        libros_prestados = [l.to_dict() for l in socio.prestamos if not l.disponible]
        if libros_prestados:
            resultado.append({
                "id_socio": socio.id,
                "nombre": socio.nombre,
                "email": socio.email,
                "libros_prestados": libros_prestados
            })
            
    return jsonify(resultado)