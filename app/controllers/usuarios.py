from sqlalchemy.orm import Session
from app.mysql.mysql import DatabaseClient
from app.models.usuarios import UsuariosRequest, UsuariosResponse
from app.mysql.models import Usuarios
import app.utils.vars as gb
from datetime import datetime
from datetime import timezone


class UsuariosController:
    def create_usuario(self, body: UsuariosRequest):
        """
        Creates a new Usuario in the database
        """
        body_row = Usuarios(usuario=body.usuario, password=body.password)

        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            session.add(body_row)
            session.commit()
            session.close()

        return {"status": "ok"}

    def get_all_usuarios(self):
        """
        Gets all Usuarios records
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            response = session.query(Usuarios).all()
            session.close()

        return response

    def update_usuario(self, body: UsuariosRequest, id: int):
        """
        Updates a Usuarios record by ID
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            usuario = session.query(Usuarios).get(id)
            if not usuario:
                return {"error": "Usuario not found"}

            usuario.usuario = body.usuario
            usuario.password=body.password
            session.commit()
            session.close()

        return {"status": "ok"}

    def delete_usuario(self, id: int):
        """
        Deletes a Usuarios record by ID
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            usuario = session.query(Usuarios).get(id)
            if not usuario:
                return {"error": "Usuario not found"}

            session.delete(usuario)
            session.commit()
            session.close()

        return {"status": "ok"}
    
    def verificar_usuarios(self, usuario: str, password: str) -> dict:
        """
        Verifies if the username and password are correct
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            # Busca al usuario por nombre
            usuario_db = session.query(Usuarios).filter(Usuarios.usuario == usuario).first()
            session.close()

        # Si no se encuentra el usuario o la contraseña no coincide
        if not usuario_db or usuario_db.password != password:
            return {"error": "Credenciales inválidas"}

        # Si las credenciales son válidas
        return {"status": "ok"}
    
    