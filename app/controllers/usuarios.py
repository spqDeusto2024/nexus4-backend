from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.mysql.mysql import DatabaseClient
from app.models.usuarios import UsuariosRequest, UsuariosResponse
from app.mysql.models import Usuarios
import app.utils.vars as gb
from datetime import datetime
import jwt 
from typing import Optional
from fastapi import HTTPException, status
from app.auth import create_access_token, verify_token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
        """
        Returns a hashed version of the password.

        Args:
            password (str): The plain text password.

        Returns:
            str: The hashed password.
        """
        return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Compare the plain text password with the hashed password.

        Args:
            plain_password (str): The plain text password.
            hashed_password (str): The hashed password.

        Returns:
            bool: True if the password matches, False otherwise
        """
        return pwd_context.verify(plain_password, hashed_password)

class UsuariosController:

    def create_usuario(self, body: UsuariosRequest):
        """
        Creates a new Usuario in the database.

        Args:
            body (UsuariosRequest): The request body containing the usuario data.

        Returns:
            dict: A dictionary with the status of the creation operation.
        """
        # Hasheamos la contraseña antes de almacenarla
        hashed_password = hash_password(body.password)
        
        body_row = Usuarios(usuario=body.usuario, password=hashed_password)

        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            session.add(body_row)
            session.commit()
            session.close()

        return {"status": "ok"}

    def get_all_usuarios(self):
        """
        Gets all Usuario records.

        Returns:
            list: A list of all Usuario records.
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            response = session.query(Usuarios).all()
            session.close()

        return response

    def update_usuario(self, body: UsuariosRequest, id: int):
        """
        Updates a Usuario record by ID.

        Args:
            body (UsuariosRequest): The request body containing the updated usuario data.
            id (int): The ID of the usuario to update.

        Returns:
            dict: A dictionary with the status of the update operation.
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            usuario = session.query(Usuarios).get(id)
            if not usuario:
                return {"error": "Usuario not found"}

            usuario.usuario = body.usuario
            usuario.password = self.hash_password(body.password)
            session.commit()
            session.close()

        return {"status": "ok"}

    def delete_usuario(self, id: int):
        """
        Deletes a Usuario record by ID.

        Args:
            id (int): The ID of the usuario to delete.

        Returns:
            dict: A dictionary with the status of the delete operation.
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
        Verify the user's credentials.

        Args:
            usuario (str): The user's username.
            password (str): The user's password.

        Returns:
            dict: A dictionary with the user's ID and username
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            # Busca el usuario por nombre de usuario
            user = session.query(Usuarios).filter(Usuarios.usuario == usuario).first()

            # Si el usuario no existe, lanzar una excepción
            if user is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no encontrado"
                )

            # Verificar la contraseña hasheada usando la función verify_password
            if not verify_password(password, user.password):  # Aquí se utiliza verify_password
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Contraseña incorrecta"
                )

            # Si la verificación es exitosa, devolver el usuario
            return {
                "id": user.id,
                "usuario": user.usuario
            }
