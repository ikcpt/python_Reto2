from flask import Blueprint, jsonify, request
from app.services.libros_service import LibroService

api_bp = Blueprint(
    "api",
    __name__,       
    url_prefix="/api"
)

@api_bp.route("/listar", methods=["GET"])
def listar():
    libros = LibroService.obtener_todos()
    return jsonify([l.to_dict() for l in libros])