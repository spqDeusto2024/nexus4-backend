from pydantic import BaseModel

class UsuariosRequest(BaseModel):
    usuario: str
    password: str

class UsuariosResponse(UsuariosRequest):
    id: int