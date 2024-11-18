from pydantic import BaseModel

class FamiliaRequest(BaseModel):
    apellido: str
    id_estancia: int

class FamiliaResponse(FamiliaRequest):
    id: int
