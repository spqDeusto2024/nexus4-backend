from pydantic import BaseModel
from typing import Optional

class FamiliaRequest(BaseModel):
    apellido: str
class FamiliaResponse(FamiliaRequest):
    id: int
