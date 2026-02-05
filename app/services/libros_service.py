from app import db
from app.models.libro import Libro

class LibroService:
    
    @staticmethod
    def obtener_todos(busqueda=None, solo_disponibles=False):
        # Empezamos la consulta base
        query = Libro.query
        
        # Aplicamos filtro de búsqueda si existe
        if busqueda:
            query = query.filter(Libro.titulo.ilike(f'%{busqueda}%'))
        
        # Aplicamos filtro de disponibilidad
        if solo_disponibles:
            query = query.filter(Libro.disponible == True)
            
        return query.all()

    @staticmethod
    def obtener_por_id(id):
        return Libro.query.get_or_404(id)

    @staticmethod
    def crear_libro(datos_form):
        nuevo_libro = Libro(
            titulo=datos_form.titulo.data,
            autor=datos_form.autor.data,
            genero=datos_form.genero.data,
            anio=datos_form.anio.data,
            resumen=datos_form.resumen.data,
            disponible=True
        )
        db.session.add(nuevo_libro)
        db.session.commit()
        return nuevo_libro

    @staticmethod
    def editar_libro(id, datos_form):
        libro = Libro.query.get_or_404(id)
        libro.titulo = datos_form.titulo.data
        libro.autor = datos_form.autor.data
        libro.genero = datos_form.genero.data
        libro.anio = datos_form.anio.data
        libro.resumen = datos_form.resumen.data
        db.session.commit()
        return libro

    @staticmethod
    def eliminar_libro(id):
        libro = Libro.query.get_or_404(id)
        db.session.delete(libro)
        db.session.commit()

    @staticmethod
    def prestar_libro(libro_id, socio_id):
        libro = Libro.query.get_or_404(libro_id)
        if libro.disponible:
            libro.disponible = False
            libro.socio_id = socio_id
            db.session.commit()
            return True
        return False

    @staticmethod
    def devolver_libro(libro_id):
        libro = Libro.query.get_or_404(libro_id)
        libro.disponible = True
        libro.socio_id = None
        db.session.commit()