from sqlalchemy.orm import Session
from app.mysql.mysql import DatabaseClient
from app.models.estancia import EstanciaRequest, EstanciaResponse
from app.mysql.models import Estancia
import app.utils.vars as gb


class EstanciaController:
    def create_estancia(self, body: EstanciaRequest):
        """
        Creates a new Estancia in the database

        Args:
            body (EstanciaRequest): The request body containing the estancia data.

        Returns:
            dict: A dictionary with the status of the update operation.
        """
        body_row = Estancia(
            nombre=body.nombre,
            categoria=body.categoria,
            personas_actuales= body.personas_actuales,
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

        Returns:
            list: A list of all Estancia records.
        
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            response = session.query(Estancia).all()
            session.close()

        return response

    def update_estancia(self, body: EstanciaRequest, id: int):
        """
        Updates an Estancia record by ID.

        Args:
            body (EstanciaRequest): The request body containing the updated estancia data.
            id (int): The ID of the estancia to update.

        Returns:
            dict: A dictionary with the status of the update operation.
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
        Deletes an Estancia record by ID.

        Args:
            id (int): The ID of the estancia to delete.

        Returns:
            dict: A dictionary with the status of the delete operation.
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
    

    def consultar_disponibilidad(self, id: int, numero_personas: int):
        """
        Checks the availability of an Estancia for a given number of people.

        Args:
            id (int): The ID of the estancia to check.
            numero_personas (int): The number of people to check availability for.

        Returns:
            bool: True if the estancia can accommodate the number of people, False otherwise.
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            estancia = session.query(Estancia).get(id)
            if not estancia:
                return {"error": "Estancia not found"}

            disponible = estancia.capacidad_max >= numero_personas
            session.close()

        return disponible
    
    def asignar_estancia(self, inquilino_id: int, estancia_id: int):
        """
        Assigns a tenant to a specific estancia.

        Args:
            inquilino_id (int): The ID of the tenant to assign.
            estancia_id (int): The ID of the estancia to assign the tenant to.

        Returns:
            dict: A dictionary with the status of the assignment operation.
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            # Buscar al inquilino por ID
            inquilino = session.query(Inquilino).get(inquilino_id)
            if not inquilino:
                return {"error": "Inquilino no encontrado"}

            # Buscar la estancia por ID
            estancia = session.query(Estancia).get(estancia_id)
            if not estancia:
                return {"error": "Estancia no encontrada"}

            # Verificar si la estancia ha alcanzado su capacidad máxima
            if estancia.capacidad_maxima_alcanzada:
                return {"error": "La capacidad máxima de la estancia ha sido alcanzada"}

            # Asignar la estancia al inquilino
            inquilino.estancia_id = estancia_id
            estancia.personas_actuales += 1
            estancia.actualizar_capacidad_maxima_alcanzada()

            session.commit()
            session.close()

        return {"status": "Estancia asignada exitosamente", "inquilino_id": inquilino_id, "estancia_id": estancia_id}