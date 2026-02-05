from flask import Blueprint, render_template, redirect, url_for, flash
from app.services.socio_service import SocioService 
from app.forms.socio_form import SocioForm
from app.forms.busqueda_socio_form import BusquedaSocioForm

socios_bp = Blueprint('socios', __name__, url_prefix='/socios')

@socios_bp.route('/grid')
def grid():
    socios = SocioService.obtener_todos()
    return render_template('paginas/socios/sociosGrid.html', socios=socios)

@socios_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    form = SocioForm()
    if form.validate_on_submit():
        SocioService.crear_socio(form)
        flash('Socio registrado', 'success')
        return redirect(url_for('socios.grid'))
    return render_template('paginas/socios/socio_crear.html', form=form)

@socios_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    socio = SocioService.obtener_por_id(id)
    form = SocioForm(obj=socio)
    
    if form.validate_on_submit():
        SocioService.editar_socio(id, form)
        flash('Socio actualizado', 'success')
        return redirect(url_for('socios.grid'))
    
    return render_template('paginas/socios/socio_editar.html', form=form, socio=socio)