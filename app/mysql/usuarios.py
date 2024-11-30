from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, TIMESTAMP
from sqlalchemy.orm import relationship
from app.mysql.base import Base

class Usuarios(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    usuario = Column(String(50))
    password= Column(String(255))

    def __repr__(self) -> str:
        return f"<Usuarios(id='{self.id}', usuario='{self.usuario}', password='{self.password}')>"