from pydantic import BaseModel
from typing import Optional

class InquilinoRequest(BaseModel):
    nombre: str
    categoria: str
    nacimiento: Optional[str]  # ISO 8601 timestamp
    muerte: Optional[str]
    familia_id: int
    empleo_id: int
    roles_id: int
    id_estancia: Optional[int] = None

 
class InquilinoResponse(InquilinoRequest):
    id: int
