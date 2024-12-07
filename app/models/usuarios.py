from pydantic import BaseModel

class UsuariosRequest(BaseModel):
    """
    Represents a request to create or update a Usuario record.

    Attributes:
        usuario (str): The username of the Usuario.
        password (str): The password of the Usuario
    """
    usuario: str
    password: str

class UsuariosResponse(UsuariosRequest):
    """
    Represents a response containing Usuario data.

    Attributes:
        id (int): The ID of the Usuario.
    """
    id: int
