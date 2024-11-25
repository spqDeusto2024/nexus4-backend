from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, TIMESTAMP
from sqlalchemy.orm import relationship
from app.mysql.base import Base

class Inquilino(Base):
    __tablename__ = "inquilino"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    categoria = Column(String(50))
    nacimiento = Column(TIMESTAMP)
    muerte = Column(TIMESTAMP)
    familia_id = Column(Integer, ForeignKey("familia.id"))
    empleo_id = Column(Integer, ForeignKey("empleo.id"))
    roles_id = Column(Integer, ForeignKey("roles.id"))
    id_estancia = Column(Integer, ForeignKey("estancia.id"))
    
    def __repr__(self) -> str:
        return (
            f"<Inquilino(id='{self.id}', nombre='{self.nombre}', categoria='{self.categoria}', "
            f"nacimiento='{self.nacimiento}', muerte='{self.muerte}', "
            f"familia_id='{self.familia_id}', empleo_id='{self.empleo_id}', roles_id='{self.roles_id}', id_estancia='{self.id_estancia}'))>"
        )