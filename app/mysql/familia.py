from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, TIMESTAMP
from sqlalchemy.orm import relationship
from app.mysql.base import Base


class Familia(Base):
    __tablename__ = "familia"
    id = Column(Integer, primary_key=True)
    apellido = Column(String(50))

    def __repr__(self) -> str:
        return f"<Familia(id='{self.id}', apellido='{self.apellido}'>" 