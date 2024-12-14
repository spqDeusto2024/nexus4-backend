from pydantic import BaseModel

class RecursoRequest(BaseModel):
    """
    Represents a request to create or update a Recurso record.

    Attributes:
    ----------
        nombre (str): The name of the Recurso.
        capacidad_min (int): The minimum capacity of the Recurso.
        capacidad_max (int): The maximum capacity of the Recurso.
        capacidad_actual (int): The current capacity of the Recurso.
        capacidad_maxima_alcanzada (bool): Whether the maximum capacity of the Recurso has been reached.
        capacidad_minima_alcanzada (bool): Whether the minimum capacity of the Recurso has been reached.
    """
    nombre: str
    capacidad_min: int
    capacidad_max: int
    capacidad_actual: int
    capacidad_maxima_alcanzada: bool=False
    capacidad_minima_alcanzada: bool=False

class RecursoResponse(RecursoRequest):
    """
    Represents a response containing Recurso data.

    Attributes:
    ----------
        id (int): The ID of the Recurso.
    """
    id: int
