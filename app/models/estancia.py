from pydantic import BaseModel

class EstanciaRequest(BaseModel):
    nombre: str
    categoria: str
    personas_actuales : int
    capacidad_max: int
    recurso_id: int

class EstanciaResponse(EstanciaRequest):
    id: int
 