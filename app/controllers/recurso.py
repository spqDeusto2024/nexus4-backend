from sqlalchemy.orm import Session
from app.mysql.estancia import Estancia
from app.mysql.mysql import DatabaseClient
from app.models.recurso import RecursoRequest, RecursoResponse
from app.mysql.models import Recurso
import app.utils.vars as gb


class RecursoController:
    def create_recurso(self, body: RecursoRequest):
        """
        Creates a new Recurso in the database

        Args:
            body (RecursoRequest): The request body containing the recurso data.

        Returns:
            dict: A dictionary with the status of the creation operation.
        """
        body_row = Recurso(
            nombre=body.nombre,
            capacidad_min=body.capacidad_min,
            capacidad_max=body.capacidad_max,
            capacidad_actual=body.capacidad_actual,
        )

        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            session.add(body_row)
            session.commit()
            session.close()

        return {"status": "ok"}

    def get_all_recursos(self):
        """
        Gets all Recurso records

        Returns:
            list: A list of all Recurso records.

        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            response = session.query(Recurso).all()
            session.close()

        return response

    def update_recurso(self, body: RecursoRequest, id: int):
        """
        Updates a Recurso record by ID

        Args:
            body (RecursoRequest): The request body containing the updated recurso data.
            id (int): The ID of the recurso to update.

        Returns:
            dict: A dictionary with the status of the update operation.
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            recurso = session.get(Recurso,id)
            if not recurso:
                return {"error": "Recurso not found"}

            recurso.nombre = body.nombre
            recurso.capacidad_min = body.capacidad_min
            recurso.capacidad_max = body.capacidad_max
            recurso.capacidad_actual = body.capacidad_actual
            session.commit()
            session.close()

        return {"status": "ok"}

    def delete_recurso(self, id: int):
        """
        Deletes a Recurso record by ID

        Args:
            id (int): The ID of the recurso to delete.
        
        Returns:
            dict: A dictionary with the status of the delete operation.
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            recurso = session.get(Recurso, id)
            if not recurso:
                return {"error": "Recurso not found"}
            
            # Suponiendo que existe una tabla `OtraTabla` con una clave foránea hacia `Recurso`
            session.query(Estancia).filter(Estancia.recurso_id == id).delete()
            session.delete(recurso)
            session.commit()
            session.close()

        return {"status": "ok"}
    
    def check_recurso_status(self, id: int):
        """
        Checks if a Recurso record is within the appropriate capacity range

        Args:
            id (int): The ID of the recurso to check.

        Returns:
            dict: A dictionary with the status of the recurso.
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            recurso = session.get(Recurso, id)
            if not recurso:
                return {"error": "Recurso not found"}
            
            if recurso.capacidad_minima_alcanzada:
                return {"status": "alert", "message": "Capacidad actual por debajo del mínimo"}
            elif recurso.capacidad_maxima_alcanzada:
                return {"status": "alert", "message": "Capacidad actual por encima del máximo"}
            else:
                return {"status": "ok", "message": "Capacidad actual dentro del rango"}
    
    def modify_recurso(self, id: int, cantidad: int):
        """
        Modifies the capacidad_actual of a Recurso record by ID

        Args:
            id (int): The ID of the recurso to modify.
            cantidad (int): The amount to add or remove from the recurso's capacidad_actual.

        Returns:
            dict: A dictionary with the status of the modification operation.
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            recurso = session.get(Recurso, id)
            if not recurso:
                return {"error": "Recurso not found"}

            capacidad_anterior = recurso.capacidad_actual
            nueva_capacidad = recurso.capacidad_actual + cantidad
            if nueva_capacidad > recurso.capacidad_max:
                return {"error": "No se puede añadir tanta cantidad"}
            if nueva_capacidad < recurso.capacidad_min:
                return {"error": "No se puede retirar tanta cantidad"}

            recurso.capacidad_actual = nueva_capacidad
            recurso.actualizar_capacidad_maxima_alcanzada()
            recurso.actualizar_capacidad_minima_alcanzada()
            session.commit()

             # Accede a los atributos antes de cerrar la sesión
            nombre_recurso = recurso.nombre
            session.close()


    

        return {
            "status": "ok",
            "message": f'La capacidad de "{nombre_recurso}" ha pasado de {capacidad_anterior} a {nueva_capacidad}.'
        }