from pydantic import BaseModel

class RecursoRequest(BaseModel):
    nombre: str
    capacidad_min: int
    capacidad_max: int
    capacidad_actual: int
    capacidad_maxima_alcanzada: bool=False
    capacidad_minima_alcanzada: bool=False

class RecursoResponse(RecursoRequest):
    id: int
