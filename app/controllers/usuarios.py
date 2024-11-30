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
        Devuelve una versión hasheada de la contraseña.
        """
        return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Compara una contraseña en texto plano con una contraseña hasheada.
        """
        return pwd_context.verify(plain_password, hashed_password)

class UsuariosController:

    def create_usuario(self, body: UsuariosRequest):
        """
        Crea un nuevo Usuario en la base de datos con la contraseña hasheada.
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
        Obtiene todos los registros de Usuarios.
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            response = session.query(Usuarios).all()
            session.close()

        return response

    def update_usuario(self, body: UsuariosRequest, id: int):
        """
        Actualiza un registro de Usuario por su ID.
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            usuario = session.query(Usuarios).get(id)
            if not usuario:
                return {"error": "Usuario no encontrado"}

            usuario.usuario = body.usuario
            usuario.password = hash_password(body.password)  
            session.commit()
            session.close()

        return {"status": "ok"}

    def delete_usuario(self, id: int):
        """
        Elimina un registro de Usuario por su ID.
        """
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            usuario = session.query(Usuarios).get(id)
            if not usuario:
                return {"error": "Usuario no encontrado"}

            session.delete(usuario)
            session.commit()
            session.close()

        return {"status": "ok"}
    
    def verificar_usuarios(self, usuario: str, password: str) -> dict:
        """
        Verifica si las credenciales del usuario son correctas.
        Si es así, devuelve el usuario con su id.
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
