from pydantic import BaseModel

class UserRequest(BaseModel):
  """
  Represents a request to create or update a User record.

  Attributes:
      username (str): The username of the User.
      fullname (str): The full name of the User.
      age (int): The age of the User.
  """
  name: str
  fullname: str
  age: int
  
class DeleteRequest(BaseModel):
  """
  Represents a request to delete a User record.

  Attributes:
      id (int): The ID of the User.
  """
  id: int
  
class UpdateRequest(BaseModel):
  """
  Represents a request to update a User record.

  Attributes:
      id (int): The ID of the User.
      update (UserRequest): The request body containing the updated user data.
  """
  id: int
  update: UserRequest