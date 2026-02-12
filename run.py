from app import create_app, db
from app.services.auth_service import AuthService

app = create_app()

def crear_admin_si_no_existe():
    with app.app_context():
        db.create_all()
        admin = AuthService.obtener_por_username('admin')
        if not admin:  
            print("Usuario 'admin' no encontrado. Creando...")
            AuthService.crear_usuario('admin', 'admin@biblioteca.com', '1234')
            print("Administrador creado con éxito.")
        else:
            print("ℹEl usuario 'admin' ya existe.")

if __name__ == "__main__":
    crear_admin_si_no_existe()
    app.run(debug=True)