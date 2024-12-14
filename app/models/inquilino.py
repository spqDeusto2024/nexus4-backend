from pydantic import BaseModel
from typing import Optional

class InquilinoRequest(BaseModel):
    """
    Represents a request to create or update an Inquilino record.

    Attributes:
    ----------
        nombre (str): The name of the Inquilino.
        categoria (str): The category of the Inquilino.
        nacimiento (str): The birth date of the Inquilino.
        muerte (str): The death date of the Inquilino.
        familia_id (int): The ID of the family associated with the Inquilino.
        empleo_id (int): The ID of the job associated with the Inquilino.
        roles_id (int): The ID of the roles associated with the Inquilino.
        id_estancia (int): The ID of the stay associated with the Inquilino.
    """

    nombre: str
    categoria: str
    nacimiento: Optional[str]  # ISO 8601 timestamp
    muerte: Optional[str]
    familia_id: int
    empleo_id: int
    roles_id: int
    id_estancia: Optional[int] = None

 
class InquilinoResponse(InquilinoRequest):
    """
    Represents a response containing Inquilino data.

    Attributes:
    ----------
        id (int): The ID of the Inquilino.
    """
    
    id: int
