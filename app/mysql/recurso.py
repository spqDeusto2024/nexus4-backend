from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, TIMESTAMP, Boolean
from sqlalchemy.orm import relationship
from app.mysql.base import Base

class Recurso(Base):
    __tablename__ = "recurso"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    capacidad_min = Column(Integer)
    capacidad_max = Column(Integer)
    capacidad_actual = Column(Integer)
    capacidad_maxima_alcanzada = Column(Boolean, default=False)
    capacidad_minima_alcanzada = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return (
            f"<Recurso(id='{self.id}', nombre='{self.nombre}', capacidad_min='{self.capacidad_min}', "
            f"capacidad_max='{self.capacidad_max}', capacidad_actual='{self.capacidad_actual}', "
            f"capacidad_maxima_alcanzada='{self.capacidad_maxima_alcanzada}', capacidad_minima_alcanzada='{self.capacidad_minima_alcanzada}')>"
        )

    def actualizar_capacidad_maxima_alcanzada(self):
        self.capacidad_maxima_alcanzada = self.capacidad_actual >= self.capacidad_max

    def actualizar_capacidad_minima_alcanzada(self):
        self.capacidad_minima_alcanzada = self.capacidad_actual <= self.capacidad_min