from pydantic import BaseModel

class RecursoRequest(BaseModel):
    nombre: str
    capacidad_min: int
    capacidad_max: int
    capacidad_actual: int

class RecursoResponse(RecursoRequest):
    id: int
