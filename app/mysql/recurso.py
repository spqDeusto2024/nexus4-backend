from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, TIMESTAMP
from sqlalchemy.orm import relationship
from app.mysql.base import Base

class Recurso(Base):
    __tablename__ = "recurso"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    capacidad_min = Column(Integer)
    capacidad_max = Column(Integer)
    capacidad_actual = Column(Integer)

    def __repr__(self) -> str:
        return (
            f"<Recurso(id='{self.id}', nombre='{self.nombre}', capacidad_min='{self.capacidad_min}', "
            f"capacidad_max='{self.capacidad_max}', capacidad_actual='{self.capacidad_actual}')>"
        )