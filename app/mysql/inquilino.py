from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, TIMESTAMP
from sqlalchemy.orm import relationship
from app.mysql.base import Base

class Inquilino(Base):
    """
    Representa la tabla 'inquilino' en la base de datos 

    Attributes:
    ----------
    id : int
        ID del inquilino
    nombre : str
        Nombre del inquilino
    categoria : str
        Categoría del inquilino
    nacimiento : TIMESTAMP
        Fecha de nacimiento del inquilino
    muerte : TIMESTAMP
        Fecha de muerte del inquilino
    familia_id : int
        ID de la familia asociada
    empleo_id : int
        ID del empleo asociado
    roles_id : int
        ID del rol asociado
    id_estancia : int
        ID de la estancia asociada
    """
    
    __tablename__ = "inquilino"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    categoria = Column(String(50))
    nacimiento = Column(TIMESTAMP)
    muerte = Column(TIMESTAMP, nullable=True)
    familia_id = Column(Integer, ForeignKey("familia.id", ondelete="CASCADE"))
    empleo_id = Column(Integer, ForeignKey("empleo.id", ondelete="CASCADE"))
    roles_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"))
    id_estancia = Column(Integer, ForeignKey("estancia.id", ondelete="CASCADE"))
    
    def __repr__(self) -> str:
        return (
            f"<Inquilino(id='{self.id}', nombre='{self.nombre}', categoria='{self.categoria}', "
            f"nacimiento='{self.nacimiento}', muerte='{self.muerte}', "
            f"familia_id='{self.familia_id}', empleo_id='{self.empleo_id}', roles_id='{self.roles_id}', id_estancia='{self.id_estancia}'))>"
        )