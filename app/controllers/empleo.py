from sqlalchemy.orm import Session
from app.mysql.mysql import DatabaseClient
from app.models.empleo import EmpleoRequest, EmpleoResponse
from app.mysql.models import Empleo
import app.utils.vars as gb


class EmpleoController:
    def create_empleo(self, body: EmpleoRequest):
        """
        Creates a new Empleo in the database

        Args:
            body (EmpleoRequest): The request body containing the empleo data.

        Returns:
            dict: A dictionary with the status of the update
        """
        body_row = Empleo(
            empleo=body.empleo,
            edad_minima=body.edad_minima,
            id_estancia=body.id_estancia,
        )

        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            session.add(body_row)
            session.commit()
            session.close()

        return {"status": "ok"}

    def get_all_empleos(self):
        """
        Gets all Empleo records

        Returns:
            list: A list of all Empleo records.
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            response = session.query(Empleo).all()
            session.close()

        return response

    def update_empleo(self, body: EmpleoRequest, id: int):
        """
        Updates an Empleo record by ID.

        Args:
            body (EmpleoRequest): The request body containing the updated empleo data.
            id (int): The ID of the empleo to update.

        Returns:
            dict: A dictionary with the status of the update operation.
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            empleo = session.query(Empleo).get(id)
            if not empleo:
                return {"error": "Empleo not found"}

            empleo.empleo = body.empleo
            empleo.edad_minima = body.edad_minima
            empleo.id_estancia = body.id_estancia
            session.commit()
            session.close()

        return {"status": "ok"}

    def delete_empleo(self, id: int):
        """
        Deletes an Empleo record by ID.

        Args:
            id (int): The ID of the empleo to delete.

        Returns:
            dict: A dictionary with the status of the delete operation.
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            empleo = session.query(Empleo).get(id)
            if not empleo:
                return {"error": "Empleo not found"}

            session.delete(empleo)
            session.commit()
            session.close()

        return {"status": "ok"}
