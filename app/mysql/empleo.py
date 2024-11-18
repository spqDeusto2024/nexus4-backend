from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, TIMESTAMP
from sqlalchemy.orm import relationship
from app.mysql.base import Base

class Empleo(Base):
    __tablename__ = "empleo"
    id = Column(Integer, primary_key=True)
    empleo = Column(String(50))
    edad_minima = Column(Integer)
    id_estancia = Column(Integer, ForeignKey("estancia.id"))

    def __repr__(self) -> str:
        return (
            f"<Empleo(id='{self.id}', empleo='{self.empleo}', edad_minima='{self.edad_minima}', "
            f"id_estancia='{self.id_estancia}')>"
        )