from app import create_app, db
from app.services.auth_service import AuthService

app = create_app()
# Crear el usuario admin si no existe
def crear_admin_si_no_existe():
    with app.app_context():
        admin = AuthService.obtener_por_username('admin')
        if not admin:
            AuthService.crear_usuario('admin', 'admin@biblioteca.com', '1234')
        else:
            print("ℹ️ El usuario 'admin' ya existe.")

if __name__ == "__main__":
    crear_admin_si_no_existe()
    app.run(debug=True)