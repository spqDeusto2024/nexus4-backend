import app.models.models as models
import app.mysql.models as mysql_models
from app.mysql.mysql import DatabaseClient

import app.utils.vars as gb
from sqlalchemy.orm import Session


class Controllers:
  def __init__(self) -> None:
    pass
  
  def healthz(self):
    """
    Checks server status

    Returns:
      dict: A dictionary with the server status.
    """
    return {"status": "ok"}
  
  def create_user(self, body: models.UserRequest):
    """
    Creates new user in  the database

    Args:
            body (models.UserRequest): The request body containing the user data.

    Returns:
      dict: A dictionary with the status of the creation operation.
    """
    body_row = mysql_models.User(name=body.name, fullname=body.fullname, age=body.age)
    
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      session.add(body_row)
      session.commit()
      session.close()
  
    return {"status": "ok"}
  
  def get_all(self):
    """
    Gets all users

    Returns:
      list: A list of all user records.
    """
    db = DatabaseClient(gb.MYSQL_URL)
    response: list = []
    with Session(db.engine) as session:
      response = session.query(mysql_models.User).all()
      session.close()
      
    return response
  
  def delete_user(self, id: int):
    """
    Deletes user by its UID

    Args:
      id (int): The UID of the user to delete.

    Returns:
      dict: A dictionary with the status of the delete operation.
    """
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      userToBeDeleted = session.query(mysql_models.User).get(id)
      session.delete(userToBeDeleted)
      session.commit()
      session.close()
      
    return {"status": "ok"}
  
  def update_user(self, body: models.UpdateRequest):
    """
    Updates user by its ID

    Args:
      body (models.UpdateRequest): The request body containing the updated user data.

    Returns:
      dict: A dictionary with the status of the update operation.
    """
    db = DatabaseClient(gb.MYSQL_URL)
    with Session(db.engine) as session:
      user: mysql_models.User = session.query(mysql_models.User).get(body.id)
      user.name = body.update.name
      user.fullname = body.update.fullname
      user.age = body.update.age
      session.dirty
      session.commit()
      session.close()
      
    return {"status": "ok"}
  
