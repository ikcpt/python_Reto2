from flask import Blueprint, jsonify, request
# CORRECCIÓN: Importamos la clase LibroService, no la función suelta
from app.services.libros_service import LibroService

api_bp = Blueprint(
    "api",
    __name__,       
    url_prefix="/api"
)

@api_bp.route("/listar", methods=["GET"])
def listar():
    # CORRECCIÓN: Llamamos al método estático de la clase
    # Antes: libros = listar_libros()
    libros = LibroService.obtener_todos()
    
    # Esto asume que tu modelo Libro tiene el método .to_dict() (Requisito R21)
    return jsonify([l.to_dict() for l in libros])