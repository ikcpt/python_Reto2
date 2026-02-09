from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.services.libros_service import LibroService
from app.forms.libro_form import LibroForm
from app.forms.prestar_libro_form import PrestarLibroForm
from app.forms.busqueda_libro_form import BusquedaLibroForm

libros_bp = Blueprint('libros', __name__, url_prefix='/libros')

@libros_bp.route('/grid')
def grid():
    busqueda = request.args.get('search', '')
    solo_disponibles = request.args.get('disponibles')
    
    libros = LibroService.obtener_todos(busqueda, solo_disponibles)
    
    return render_template('paginas/libros/librosGrid.html', libros=libros)

@libros_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = LibroForm()
    if form.validate_on_submit():
        LibroService.crear_libro(form)
        flash('Libro creado correctamente', 'success')
        return redirect(url_for('libros.grid'))
    return render_template('paginas/libros/libro_crear.html', form=form)

@libros_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    libro = LibroService.obtener_por_id(id)
    form = LibroForm(obj=libro)
    
    if form.validate_on_submit():
        LibroService.editar_libro(id, form)
        flash('Libro actualizado', 'success')
        return redirect(url_for('libros.grid'))
        
    return render_template('paginas/libros/libro_editar.html', form=form, libro=libro)

@libros_bp.route('/eliminar/<int:id>')
def eliminar(id):
    LibroService.eliminar_libro(id)
    flash('Libro eliminado', 'danger')
    return redirect(url_for('libros.grid'))

@libros_bp.route('/prestar/<int:id>', methods=['GET', 'POST'])
def prestar(id):
    libro = LibroService.obtener_por_id(id)
    form = PrestarLibroForm()
    
    if form.validate_on_submit():
        LibroService.prestar_libro(id, form.socio_id.data)
        flash('Libro prestado correctamente', 'success')
        return redirect(url_for('libros.grid'))
        
    return render_template('paginas/libros/prestar.html', form=form, libro=libro)

@libros_bp.route('/devolver/<int:id>')
def devolver(id):
    LibroService.devolver_libro(id)
    flash('Libro devuelto a la biblioteca', 'info')
    return redirect(url_for('libros.grid'))