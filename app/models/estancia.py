from pydantic import BaseModel

class EstanciaRequest(BaseModel):
    """
    Represents a request to create or update an Estancia record.

    Attributes:
    ----------
        nombre (str): The name of the Estancia.
        categoria (str): The category of the Estancia.
        personas_actuales (int): The number of people currently in the Estancia.
        capacidad_max (int): The maximum capacity of the Estancia.
        recurso_id (int): The ID of the resource associated with the Estancia.
        capacidad_maxima_alcanzada (bool): Whether the maximum capacity of the Estancia has
    """
    nombre: str
    categoria: str
    personas_actuales : int
    capacidad_max: int
    recurso_id: int
    capacidad_maxima_alcanzada: bool=False

class EstanciaResponse(EstanciaRequest):
    """
    Represents a response containing Estancia data.

    Attributes:
    ----------
        id (int): The ID of the Estancia.
    """
    id: int
 