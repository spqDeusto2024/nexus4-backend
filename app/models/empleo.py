from pydantic import BaseModel

class EmpleoRequest(BaseModel):
    empleo: str
    edad_minima: int
    id_estancia: int

class EmpleoResponse(EmpleoRequest):
    id: int
