from sqlalchemy.orm import Session
from app.mysql.mysql import DatabaseClient
from app.models.familia import FamiliaRequest, FamiliaResponse
from app.mysql.models import Familia
import app.utils.vars as gb


class FamiliaController:
    def create_familia(self, body: FamiliaRequest):
        """
        Creates a new Familia in the database
        """
        body_row = Familia(apellido=body.apellido, id_estancia=body.id_estancia)

        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            session.add(body_row)
            session.commit()
            session.close()

        return {"status": "ok"}

    def get_all_familias(self):
        """
        Gets all Familia records
        """
        db = DatabaseClient(gb.MYSQL_URL)
        response: list = []
        with Session(db.engine) as session:
            response = session.query(Familia).all()
            session.close()

        return response

    def update_familia(self, body: FamiliaRequest, id: int):
        """
        Updates a Familia record by ID
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            familia = session.query(Familia).get(id)
            if not familia:
                return {"error": "Familia not found"}
            
            familia.apellido = body.apellido
            familia.id_estancia = body.id_estancia
            session.commit()
            session.close()

        return {"status": "ok"}

    def delete_familia(self, id: int):
        """
        Deletes a Familia record by ID
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            familia = session.query(Familia).get(id)
            if not familia:
                return {"error": "Familia not found"}
            
            session.delete(familia)
            session.commit()
            session.close()

        return {"status": "ok"}
