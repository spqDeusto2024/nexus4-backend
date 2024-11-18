from pydantic import BaseModel
from typing import Optional

class FamiliaRequest(BaseModel):
    apellido: str
    id_estancia: Optional[int] = None

class FamiliaResponse(FamiliaRequest):
    id: int
