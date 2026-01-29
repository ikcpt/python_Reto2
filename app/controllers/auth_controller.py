from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models.usuario import Usuario
from app.forms.auth_form import LoginForm, RegistroForm
from app import db

auth_bp = Blueprint('auth', __name__)

# --- LOGIN ---
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Usuario.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Has iniciado sesion correctamente.')
            # Asegúrate de que 'libros.inicio' existe en tus rutas
            return redirect(url_for('libros.grid'))

        flash('Usuario o contraseña invalidos.')

    return render_template('paginas/auth/login.html', form=form)

# --- REGISTRO ---
@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    
    if form.validate_on_submit():
        # Comprobar si el usuario ya existe
        if Usuario.query.filter_by(username=form.username.data).first():
            flash('El usuario ya existe')
            return redirect(url_for('auth.registro'))
        
        # IMPORTANTE: Aquí guardamos username Y email
        nuevo_usuario = Usuario(
            username=form.username.data,
            email=form.email.data
        )
        nuevo_usuario.set_password(form.password.data)

        db.session.add(nuevo_usuario)
        db.session.commit()

        flash('Usuario creado. Por favor inicia sesion.')
        return redirect(url_for('auth.login'))
        
    return render_template('paginas/auth/registro.html', form=form)

# --- LOGOUT ---
@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Has cerrado sesion correctamente.')
    return redirect(url_for('auth.login'))