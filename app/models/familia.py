from pydantic import BaseModel
from typing import Optional

class FamiliaRequest(BaseModel):
    """
    Represents a request to create or update a Familia record.

    Attributes:
        apellido (str): The last name of the family.
    """
    apellido: str

class FamiliaResponse(FamiliaRequest):
    """
    Represents a response containing Familia data.

    Attributes:
        id (int): The ID of the Familia.
    """
    id: int
 