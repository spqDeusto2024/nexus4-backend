from sqlalchemy.orm import Session
from app.mysql.mysql import DatabaseClient
from app.models.inquilino import InquilinoRequest, InquilinoResponse
from app.mysql.models import Inquilino
import app.utils.vars as gb


class InquilinoController:
    def create_inquilino(self, body: InquilinoRequest):
        """
        Creates a new Inquilino in the database
        """
        body_row = Inquilino(
            nombre=body.nombre,
            categoria=body.categoria,
            nacimiento=body.nacimiento,
            muerte=body.muerte,
            familia_id=body.familia_id,
            empleo_id=body.empleo_id,
            roles_id=body.roles_id,
            id_estancia=body.id_estancia
        )

        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            session.add(body_row)
            session.commit()
            session.close()

        return {"status": "ok"}

    def get_all_inquilinos(self):
        """
        Gets all Inquilino records
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            response = session.query(Inquilino).all()
            session.close()

        return response

    def update_inquilino(self, body: InquilinoRequest, id: int):
        """
        Updates an Inquilino record by ID
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            inquilino = session.query(Inquilino).get(id)
            if not inquilino:
                return {"error": "Inquilino not found"}

            inquilino.nombre = body.nombre
            inquilino.categoria = body.categoria
            inquilino.nacimiento = body.nacimiento
            inquilino.muerte = body.muerte
            inquilino.familia_id = body.familia_id
            inquilino.empleo_id = body.empleo_id
            inquilino.roles_id = body.roles_id
            inquilino.id_estancia = body.id_estancia

            session.commit()
            session.close()

        return {"status": "ok"}

    def delete_inquilino(self, id: int):
        """
        Deletes an Inquilino record by ID
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            inquilino = session.query(Inquilino).get(id)
            if not inquilino:
                return {"error": "Inquilino not found"}

            session.delete(inquilino)
            session.commit()
            session.close()

        return {"status": "ok"}
