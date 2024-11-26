from sqlalchemy.orm import Session
from app.mysql.mysql import DatabaseClient
from app.models.recurso import RecursoRequest, RecursoResponse
from app.mysql.models import Recurso
import app.utils.vars as gb


class RecursoController:
    def create_recurso(self, body: RecursoRequest):
        """
        Creates a new Recurso in the database
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
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            response = session.query(Recurso).all()
            session.close()

        return response

    def update_recurso(self, body: RecursoRequest, id: int):
        """
        Updates a Recurso record by ID
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            recurso = session.query(Recurso).get(id)
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
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            recurso = session.query(Recurso).get(id)
            if not recurso:
                return {"error": "Recurso not found"}

            session.delete(recurso)
            session.commit()
            session.close()

        return {"status": "ok"}
    
    def check_recurso_status(self, id: int):
        """
        Checks if a Recurso record is within the appropriate capacity range
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            recurso = session.query(Recurso).get(id)
            if not recurso:
                return {"error": "Recurso not found"}

            if recurso.capacidad_actual < recurso.capacidad_min:
                return {"status": "alert", "message": "Capacidad actual por debajo del mínimo"}
            elif recurso.capacidad_actual > recurso.capacidad_max:
                return {"status": "alert", "message": "Capacidad actual por encima del máximo"}
            else:
                return {"status": "ok", "message": "Capacidad actual dentro del rango"}

