from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.decorators.auth_decorators import admin_required
from app.forms.login_form import LoginForm
from app.forms.registro_form import RegistroForm
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

# --- LOGIN ---
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = AuthService.obtener_por_username(form.username.data)

        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Has iniciado sesion correctamente.')
            return redirect(url_for('libros.grid'))

        flash('Usuario o contraseña invalidos.')

    return render_template('paginas/auth/login.html', form=form)

# --- REGISTRO ---
@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    
    if form.validate_on_submit():
        if AuthService.obtener_por_username(form.username.data):
            flash('El usuario ya existe')
            return redirect(url_for('auth.registro'))
        
        AuthService.crear_usuario(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )

        flash('Usuario creado. Por favor inicia sesion.')
        return redirect(url_for('auth.login'))
        
    return render_template('paginas/auth/registro.html', form=form)

# --- LOGOUT ---
@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Has cerrado sesion correctamente.')
    return redirect(url_for('auth.login'))