Al utilizar el proyecto hay que crear el directorio venv con :
python -m venv venv

Despues hay que instalar las dependencias con :
pip install -r requirements.txt

Siempre que se instalen nuevas dependencias hay que actualizar el archivo requirements.txt con:
pip freeze > requirements.txt

CREDENCIALES ADMINISTRADOR:
Username: admin
Password: 1234

# 📚 Sistema de Gestión de Biblioteca (Flask) - Reto 2

Aplicación web desarrollada en Python con Flask para la gestión integral de una biblioteca. Permite administrar libros, socios y gestionar el sistema de préstamos y devoluciones, con un **sistema de autenticación seguro** para proteger las operaciones administrativas.

## 🔐 Credenciales de Administrador
El sistema crea automáticamente un usuario administrador al iniciar la aplicación (`run.py`) si no existe.

* **Username:** `admin`
* **Password:** `1234`

> **Nota:** Es necesario iniciar sesión con estas credenciales para acceder a las funciones de creación, edición y eliminación.

## 🚀 Características

* **Gestión de Libros:** Alta, baja, modificación y listado de libros (Protegido por Login).
* **Gestión de Socios:** Registro y edición de usuarios/socios (Protegido por Login).
* **Sistema de Préstamos:** Asignación de libros a socios y control de stock.
* **Autenticación y Seguridad:**
    * Sistema de Login/Logout con `Flask-Login`.
    * Protección de rutas mediante decoradores personalizados (`@admin_required`).
    * Hashing de contraseñas para seguridad en base de datos.
* **Buscador:** Filtrado de libros por título y disponibilidad.
* **Arquitectura Limpia:** Separación de lógica mediante el patrón **Service Layer**.
* **API REST:** Endpoint JSON (`/api/listar`) para consumo externo.

## 🛠️ Tecnologías Utilizadas

* **Python 3**
* **Flask** (Framework Web)
* **Flask-SQLAlchemy** (ORM para base de datos)
* **Flask-Login** (Gestión de sesiones de usuario)
* **Flask-WTF** (Formularios y validación CSRF)
* **Werkzeug Security** (Encriptación de contraseñas)
* **Jinja2** (Motor de plantillas HTML)
* **SQLite** (Base de datos ligera)

## 🏗️ Arquitectura del Proyecto

El proyecto sigue el patrón **MVC (Modelo-Vista-Controlador)** extendido con una capa de **Servicios** y **Decoradores** para mantener el código modular y escalable.

* **Controllers:** Manejan las rutas y la respuesta HTTP. Utilizan los servicios.
* **Services:** Contienen la lógica pura del negocio (CRUD, validaciones complejas).
* **Models:** Representación de las tablas (Libros, Socios, Usuarios).
* **Decorators:** Middleware personalizado para verificar permisos de administrador.

### Estructura de Carpetas Actualizada
```text
python_Reto2/
├── app/
│   ├── controllers/   # Auth, Libros, Socios, Navigation, API
│   ├── models/        # Modelos de BD (Libro, Socio, Usuario)
│   ├── services/      # Lógica de negocio (AuthService, LibroService...)
│   ├── decorators/    # Decoradores de permisos (admin_required)
│   ├── forms/         # Formularios WTForms (Login, Registro, Libros...)
│   ├── templates/     # Vistas HTML (Jinja2)
│   └── static/        # CSS, JS, Imágenes
├── run.py             # Punto de entrada (Crea DB y Admin automáticos)
└── requirements.txt   # Dependencias del proyecto