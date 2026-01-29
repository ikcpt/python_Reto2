from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.models.libro import Libro
from app.models.socio import Socio
from app.forms.libro_form import LibroForm, PrestarLibroForm

libros_bp = Blueprint('libros', __name__, url_prefix='/libros')

@libros_bp.route('/grid')
def grid():
    libros = Libro.query.all()
    # CAMBIO AQUÍ: Usamos tu nombre real 'librosGrid.html'
    return render_template('paginas/libros/librosGrid.html', libros=libros)

@libros_bp.route('/listado')
def listar():
    libros = Libro.query.all()
    # CAMBIO AQUÍ: Asumo que 'libros.html' es tu lista simple
    return render_template('paginas/libros/libros.html', libros=libros)

@libros_bp.route('/crear', methods=['GET', 'POST'])
@login_required 
def crear():
    form = LibroForm()
    if form.validate_on_submit():
        nuevo_libro = Libro(
            titulo=form.titulo.data,
            autor=form.autor.data,
            genero=form.genero.data,
            anio=form.anio.data,
            resumen=form.resumen.data,
            disponible=True
        )
        db.session.add(nuevo_libro)
        db.session.commit()
        flash('Libro creado correctamente')
        return redirect(url_for('libros.grid'))
    
    return render_template('paginas/libros/libro_crear.html', form=form)

@libros_bp.route('/prestar/<int:id>', methods=['GET', 'POST'])
@login_required
def prestar(id):
    libro = Libro.query.get_or_404(id)
    form = PrestarLibroForm()
    
    socios = Socio.query.all()
    form.socio_id.choices = [(s.id, f"{s.nombre} ({s.email})") for s in socios]

    if form.validate_on_submit():
        libro.socio_id = form.socio_id.data
        libro.disponible = False
        db.session.commit()
        flash(f'Libro prestado correctamente')
        return redirect(url_for('libros.grid'))
    
    return render_template('paginas/libros/libro_prestar.html', form=form, libro=libro)

@libros_bp.route('/devolver/<int:id>')
@login_required
def devolver(id):
    libro = Libro.query.get_or_404(id)
    if not libro.disponible:
        libro.socio_id = None
        libro.disponible = True
        db.session.commit()
        flash(f'Libro devuelto correctamente. ¡Gracias por tu prestamo!')
        
    return redirect(url_for('libros.grid'))