from functools import wraps
from flask import abort, flash, redirect, url_for
from flask_login import current_user

# Este es tu decorador personalizado (R29)
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # 1. Primero comprobamos si está logueado
        if not current_user.is_authenticated:
            flash("Debes iniciar sesión para acceder aquí.", "warning")
            return redirect(url_for('auth.login'))
        
        # 2. Comprobamos si es el administrador
        # AJUSTA ESTO: Si tu usuario admin se llama 'admin' o tiene un email específico
        # Aquí asumimos que el nombre del usuario logueado es 'admin' (como en tu captura)
        if current_user.username.lower() != 'admin':
            abort(403) # Error 403: Prohibido (Forbidden)
            
        return f(*args, **kwargs)
    return decorated_function