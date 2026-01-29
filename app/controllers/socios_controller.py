from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.models.socio import Socio
from app.forms.socio_form import SocioForm

# Definimos el Blueprint
socios_bp = Blueprint('socios', __name__, url_prefix='/socios')

@socios_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    form = SocioForm()
    
    if form.validate_on_submit():
        # Verificamos si el email ya existe para no duplicar
        socio_existente = Socio.query.filter_by(email=form.email.data).first()
        if socio_existente:
            flash('Error: Ya existe un socio con ese email.', 'danger')
            return render_template('paginas/socios/crear_socio.html', form=form)

        # Creamos el nuevo socio
        nuevo_socio = Socio(
            nombre=form.nombre.data,
            email=form.email.data
        )
        
        db.session.add(nuevo_socio)
        db.session.commit()
        
        flash('¡Socio registrado correctamente!', 'success')
        # Redirigimos al inicio porque no tenemos lista de socios aún
        return redirect(url_for('navigation.inicio'))
        
    return render_template('paginas/socios/crear_socio.html', form=form)