from pydantic import BaseModel

class RolesRequest(BaseModel):
    nombre: str

class RolesResponse(RolesRequest):
    id: int
