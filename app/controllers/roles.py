from sqlalchemy.orm import Session
from app.mysql.mysql import DatabaseClient
from app.models.roles import RolesRequest, RolesResponse
from app.mysql.models import Roles
import app.utils.vars as gb


class RolesController:
    def create_role(self, body: RolesRequest):
        """
        Creates a new Role in the database
        """
        body_row = Roles(nombre=body.nombre)

        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            session.add(body_row)
            session.commit()
            session.close()

        return {"status": "ok"}

    def get_all_roles(self):
        """
        Gets all Role records
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            response = session.query(Roles).all()
            session.close()

        return response

    def update_role(self, body: RolesRequest, id: int):
        """
        Updates a Role record by ID
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            role = session.query(Roles).get(id)
            if not role:
                return {"error": "Role not found"}

            role.nombre = body.nombre
            session.commit()
            session.close()

        return {"status": "ok"}

    def delete_role(self, id: int):
        """
        Deletes a Role record by ID
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            role = session.query(Roles).get(id)
            if not role:
                return {"error": "Role not found"}

            session.delete(role)
            session.commit()
            session.close()

        return {"status": "ok"}
