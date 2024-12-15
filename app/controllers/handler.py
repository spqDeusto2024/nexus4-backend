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
  
  
