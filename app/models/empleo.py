from pydantic import BaseModel, Field

class EmpleoRequest(BaseModel):
    """
    Data model for creating a empleo

    Attributes:
        empleo (str): Nombre del empleo
        edad_minima (int): Edad mínima requerida para el empleo
        id_estancia (int): ID de la estancia asociada
    """
    empleo: str = Field(..., description="Nombre del empleo")
    edad_minima: int = Field(..., description="Edad mínima requerida para el empleo")
    id_estancia: int = Field(..., description="ID de la estancia asociada")

    class Config:
        schema_extra = {
            "example": {
                "empleo": "Ingeniero",
                "edad_minima": 25,
                "id_estancia": 1
            }
        }

class EmpleoResponse(EmpleoRequest):
    """
    Data model for the empleo response

    Attributes:
        id (int): ID del empleo
    """
    
    id: int = Field(..., description="ID del empleo")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "empleo": "Ingeniero",
                "edad_minima": 25,
                "id_estancia": 1
            }
        }