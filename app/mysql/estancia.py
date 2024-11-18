from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, TIMESTAMP
from sqlalchemy.orm import relationship
from app.mysql.base import Base

class Estancia(Base):
    __tablename__ = "estancia"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    categoria = Column(String(50))
    capacidad_max = Column(Integer)
    recurso_id = Column(Integer, ForeignKey("recurso.id"))

    def __repr__(self) -> str:
        return (
            f"<Estancia(id='{self.id}', nombre='{self.nombre}', categoria='{self.categoria}', "
            f"capacidad_max='{self.capacidad_max}', recurso_id='{self.recurso_id}')>"
        )