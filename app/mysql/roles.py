from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, TIMESTAMP
from sqlalchemy.orm import relationship
from app.mysql.base import Base

class Roles(Base):
    """
    Representa la tabla 'roles' en la base de datos

    Attributes:
    ----------
    id : int
        ID del rol
    nombre : str
        Nombre del rol
    """
    
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))

    def __repr__(self) -> str:
        return f"<Roles(id='{self.id}', nombre='{self.nombre}')>"