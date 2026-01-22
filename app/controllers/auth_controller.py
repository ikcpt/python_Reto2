from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.models.usuario import Usuario
from app.forms.auth_form import LoginForm, RegistroForm
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', method=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Usuario.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Has iniciado sesion correctamente.')
            return redirect(url_for('libros.inicio'))

        flash('Usuario o contraseña invalidos.')

    return render_template('paginas/auth/login.html', form=form)

@auth_bp.route('/registro', method= ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Usuario.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Has iniciado sesion correctamente.')
            return redirect(url_for('libros.inicio'))
       
        flash('Usuario o contraseña invalidos.') 

    return render_template('paginas/auth/login.html', form=form)

@auth_bp.route('/registro', methods=[+'GET', 'POST'])
def registro():
    form = RegistroForm()
    
    if form.validate_on_submit():
        if Usuario.query.fiilter_by(username=form.usernma.data).fisrt():
            return redirect(url_for('auth.registro'))
        
        nuevo_usuario = Usuario(username=form.password.data)
        nuevo_usuario.set_password(form.password.data)

        db.session.add(nuevo_usuario)
        db.session.commit()

        flash('Usuario creado. Por favor inicia sesion.')
        return redirect(url_for('auth.logiin'))
    return render_template('paginas/auth/registro.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))