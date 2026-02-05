from flask import Blueprint, jsonify
from app.models.libro import Libro
from app.models.socio import Socio

# Creamos el Blueprint 'api'
api_bp = Blueprint('api_rest', __name__, url_prefix='/api')

# R21: Listar todos los libros (JSON)
@api_bp.route('/libros', methods=['GET'])
def get_libros():
    libros = Libro.query.all()
    # Usamos el método to_dict() que ya tienes en tu modelo
    return jsonify([l.to_dict() for l in libros])

# R22: Listar libros disponibles
@api_bp.route('/librosdisponibles', methods=['GET'])
def get_libros_disponibles():
    libros = Libro.query.filter_by(disponible=True).all()
    return jsonify([l.to_dict() for l in libros])

# R23: Buscar libro por título
@api_bp.route('/libros/buscar/<string:titulo>', methods=['GET'])
def buscar_libro(titulo):
    # Usamos ilike para que ignore mayúsculas/minúsculas
    libros = Libro.query.filter(Libro.titulo.ilike(f'%{titulo}%')).all()
    return jsonify([l.to_dict() for l in libros])

# R24: Socios con préstamos activos
@api_bp.route('/libros/socios/prestamos', methods=['GET'])
def get_socios_con_prestamos():
    # Buscamos socios que tengan algún préstamo (join implicito o filtrado en python)
    # Una forma eficiente en Python:
    socios = Socio.query.all()
    resultado = []
    
    for socio in socios:
        # Filtramos sus libros que NO están disponibles (prestados)
        libros_prestados = [l.to_dict() for l in socio.prestamos if not l.disponible]
        
        if libros_prestados:
            resultado.append({
                "id_socio": socio.id,
                "nombre": socio.nombre,
                "email": socio.email,
                "libros_prestados": libros_prestados
            })
            
    return jsonify(resultado)