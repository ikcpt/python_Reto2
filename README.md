Al utilizar el proyecto hay que crear el directorio venv con :
python -m venv venv

Despues hay que instalar las dependencias con :
pip install -r requirements.txt

Siempre que se instalen nuevas dependencias hay que actualizar el archivo requirements.txt con:
pip freeze > requirements.txt

# 📚 Sistema de Gestión de Biblioteca (Flask) - Reto 2

Aplicación web desarrollada en Python con Flask para la gestión integral de una biblioteca. Permite administrar libros, socios y gestionar el sistema de préstamos y devoluciones.

## 🚀 Características

* **Gestión de Libros:** Alta, baja, modificación y listado de libros.
* **Buscador:** Filtrado de libros por título y disponibilidad.
* **Gestión de Socios:** Registro y edición de usuarios/socios.
* **Préstamos:** Sistema para prestar libros a socios y registrar devoluciones.
* **Arquitectura Limpia:** Separación de lógica de negocio mediante **Servicios**.
* **API REST:** Endpoint JSON para consumo externo de datos.

## 🛠️ Tecnologías Utilizadas

* **Python 3**
* **Flask** (Framework Web)
* **SQLAlchemy** (ORM para base de datos)
* **WTForms** (Manejo y validación de formularios)
* **Jinja2** (Motor de plantillas HTML)
* **SQLite** (Base de datos)

## 🏗️ Arquitectura del Proyecto

El proyecto sigue el patrón **MVC (Modelo-Vista-Controlador)** con una capa adicional de **Servicios** para desacoplar la lógica de negocio de las rutas HTTP.

* **Controllers:** Manejan las peticiones HTTP y respuestas (`routes`). No tocan la BD directamente.
* **Services:** Contienen la lógica de negocio (Crear, buscar, prestar). Interactúan con los Modelos.
* **Models:** Definición de las tablas de la base de datos.
* **Templates:** Interfaz de usuario (HTML/CSS).

### Estructura de Carpetas
```text
python_Reto2/
├── app/
│   ├── controllers/   # Lógica de rutas (Navigation, Libros, Socios, API)
│   ├── models/        # Modelos de BD (Libro, Socio)
│   ├── services/      # Lógica de negocio (LibroService, SocioService)
│   ├── forms/         # Formularios WTForms
│   ├── templates/     # Archivos HTML (Jinja2)
│   └── static/        # CSS, JS, Imágenes
├── run.py             # Punto de entrada de la aplicación
└── requirements.txt   # Dependencias del proyecto