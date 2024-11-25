from sqlalchemy.orm import Session
from app.mysql.mysql import DatabaseClient
from app.models.estancia import EstanciaRequest, EstanciaResponse
from app.mysql.models import Estancia
import app.utils.vars as gb


class EstanciaController:
    def create_estancia(self, body: EstanciaRequest):
        """
        Creates a new Estancia in the database
        """
        body_row = Estancia(
            nombre=body.nombre,
            categoria=body.categoria,
            personas_actuales= body.categoria,
            capacidad_max=body.capacidad_max,
            recurso_id=body.recurso_id,
        )

        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            session.add(body_row)
            session.commit()
            session.close()

        return {"status": "ok"}

    def get_all_estancias(self):
        """
        Gets all Estancia records
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            response = session.query(Estancia).all()
            session.close()

        return response

    def update_estancia(self, body: EstanciaRequest, id: int):
        """
        Updates an Estancia record by ID
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            estancia = session.query(Estancia).get(id)
            if not estancia:
                return {"error": "Estancia not found"}

            estancia.nombre = body.nombre
            estancia.categoria = body.categoria
            estancia.capacidad_max = body.capacidad_max
            estancia.recurso_id = body.recurso_id
            session.commit()
            session.close()

        return {"status": "ok"}

    def delete_estancia(self, id: int):
        """
        Deletes an Estancia record by ID
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            estancia = session.query(Estancia).get(id)
            if not estancia:
                return {"error": "Estancia not found"}

            session.delete(estancia)
            session.commit()
            session.close()

        return {"status": "ok"}
    

    def consultar_disponibilidad(self, id, numero_personas):
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            estancia = session.query(Estancia).get(id)
            if not estancia:
                return {"error": "Estancia not found"}

            if estancia.personas_actuales < estancia.capacidad_max:
                return {"disponible": True}
            else:
                return {"disponible": False}
