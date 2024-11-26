from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, TIMESTAMP
from sqlalchemy.orm import relationship
from app.mysql.base import Base

class Estancia(Base):
    __tablename__ = "estancia"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    categoria = Column(String(50))
    personas_actuales = Column (Integer, default=0)
    capacidad_max = Column(Integer)
    recurso_id = Column(Integer, ForeignKey("recurso.id"))
    
    @property
    def personas_actuales_calculadas(self):
        db = DatabaseClient(gb.MYSQL_URL)
        with Session(db.engine) as session:
            count = session.query(Inquilino).filter(Inquilino.id_estancia == self.id).count()
            session.close()
        return count

    def __repr__(self) -> str:
        return (
            f"<Estancia(id='{self.id}', nombre='{self.nombre}', categoria='{self.categoria}', "
            f"capacidad_max='{self.capacidad_max}', recurso_id='{self.recurso_id}')>"
            f"personas_actuales='{self.personas_actuales_calculadas}')>"
        )