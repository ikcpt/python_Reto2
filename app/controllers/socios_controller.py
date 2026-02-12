from flask import Blueprint, render_template, redirect, url_for, flash
from app.services.socio_service import SocioService 
from app.forms.socio_form import SocioForm
from flask_login import login_required
from app.decorators.auth_decorators import admin_required

socios_bp = Blueprint('socios', __name__, url_prefix='/socios')

@socios_bp.route('/grid')
def grid():
    socios = SocioService.obtener_todos()
    return render_template('paginas/socios/sociosGrid.html', socios=socios)

@socios_bp.route('/crear', methods=['GET', 'POST'])
@login_required
@admin_required
def crear():
    form = SocioForm()
    if form.validate_on_submit():
        SocioService.crear_socio(form)
        flash('Socio registrado', 'success')
        return redirect(url_for('socios.grid'))
    return render_template('paginas/socios/socio_crear.html', form=form)

@socios_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar(id):
    socio = SocioService.obtener_por_id(id)
    form = SocioForm(obj=socio)
    
    if form.validate_on_submit():
        SocioService.editar_socio(id, form)
        flash('Socio actualizado', 'success')
        return redirect(url_for('socios.grid'))
    
    return render_template('paginas/socios/socio_editar.html', form=form, socio=socio)
    
@socios_bp.route('/eliminar/<int:id>', methods=['POST'])
@login_required
@admin_required
def eliminar(id):
    SocioService.eliminar_socio(id)
    flash('Socio eliminado', 'danger')
    return redirect(url_for('socios.grid'))