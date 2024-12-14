from pydantic import BaseModel

class RolesRequest(BaseModel):
    """
    Represents a request to create or update a Roles record.

    Attributes:
    ----------
        nombre (str): The name of the role.
    """
    nombre: str

class RolesResponse(RolesRequest):
    """
    Represents a response containing Roles data.

    Attributes:
    ----------
        id (int): The ID of the Roles.
    """
    id: int
