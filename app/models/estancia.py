from pydantic import BaseModel

class EstanciaRequest(BaseModel):
    nombre: str
    categoria: str
    personas_actuales : int
    capacidad_max: int
    recurso_id: int
    capacidad_maxima_alcanzada: bool=False

class EstanciaResponse(EstanciaRequest):
    id: int
 