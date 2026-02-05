from flask import Blueprint, render_template
from app.services.libros_service import LibroService

navigation_bp = Blueprint('navigation', __name__)

@navigation_bp.route('/')
def home():
    libros = LibroService.obtener_todos()
    return render_template('paginas/inicio.html', libros=libros)