from sqlalchemy.orm import Session
from app.mysql.mysql import DatabaseClient
from app.models.inquilino import InquilinoRequest, InquilinoResponse
from app.mysql.models import Inquilino
from app.mysql.models import Estancia
import app.utils.vars as gb
from datetime import datetime
from typing import Optional



class InquilinoController:
    def create_inquilino(self, body: InquilinoRequest):
        """
        Creates a new Inquilino in the database

        Args:
            body (InquilinoRequest): The request body containing the inquilino data.
        
        Returns:
            dict: A dictionary with the status of the creation operation.
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

        Returns:
            list: A list of all Inquilino records.

        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            response = session.query(Inquilino).all()
            session.close()

        return response

    def update_inquilino(self, body: InquilinoRequest, id: int):
        """
        Updates an Inquilino record by ID

        Args:
            body (InquilinoRequest): The request body containing the updated inquilino data.
            id (int): The ID of the inquilino to update.
        
        Returns:
            dict: A dictionary with the status of the update operation.
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

        Args:
            id (int): The ID of the inquilino to delete.

        Returns:
            dict: A dictionary with the status of the delete operation.
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
    
    def marcar_como_fallecido(self, id: int, fecha_muerte: Optional[datetime] = None):

        """
        Marks an Inquilino as death.

        Args:
            id (int): The ID of the inquilino to mark as death.
            fecha_muerte (datetime): The date of death of the inquilino.

        Returns:
            dict: A dictionary with the status of the operation
        """

        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            # Buscar al inquilino por ID
            inquilino = session.query(Inquilino).get(id)
            if not inquilino:
                return {"error": "Inquilino no encontrado"}

            # Actualizar la fecha de fallecimiento
            inquilino.muerte = fecha_muerte or datetime.now()
            session.commit()
            session.close()

        return {"status": "Inquilino marcado como fallecido", "id": id}

    def consultardisponibilidad (self, estancia_id: int):
        """
        Checks the availability of an Estancia.

        Args:
            estancia_id (int): The ID of the estancia to check.
        
        Returns:
            str: A string indicating if there is space available
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            # Buscar la estancia por ID
            estancia = session.query(Estancia).get(estancia_id)
            if not estancia:
                return {"error": "Estancia no encontrada"}

            # Obtener personas_actuales y capacidad_maxima
            personas_actuales = estancia.personas_actuales
            capacidad_max = estancia.capacidad_max
            session.commit()
            session.close()

        if personas_actuales < capacidad_max:
            return "Hay espacio disponible"
        else:
            return "No hay espacio disponible"
        