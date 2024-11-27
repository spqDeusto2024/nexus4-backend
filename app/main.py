from app.controllers.handler import Controllers
from fastapi import FastAPI, HTTPException
from typing import Union
from app.mysql.mysql import DatabaseClient
from app.mysql import Familia, Empleo, Estancia, Inquilino, Recurso, Roles
import app.utils.vars as gb
from datetime import datetime
from typing import Optional
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordRequestForm

#Import all the controllers
from app.controllers.familia import FamiliaController
from app.controllers.inquilino import InquilinoController
from app.controllers.estancia import EstanciaController
from app.controllers.empleo import EmpleoController
from app.controllers.recurso import RecursoController
from app.controllers.roles import RolesController
from app.controllers.usuarios import UsuariosController

#Import all the models
import app.models.familia as familiaModels
import app.models.empleo as empleoModels
import app.models.estancia as estanciaModels
import app.models.inquilino as inquilinoModels
import app.models.recurso as recursoModels
import app.models.roles as rolesModels
import app.models.usuarios as usuarioModels



def initialize() -> None:
  # initialize database
  dbClient = DatabaseClient(gb.MYSQL_URL)
  dbClient.init_database()
  return


app = FastAPI()
controllers = Controllers()
familia_controller = FamiliaController()
inquilino_controller = InquilinoController()
estancia_controller = EstanciaController()
empleo_controller = EmpleoController()
recurso_controller = RecursoController()
roles_controller = RolesController()
usuario_controller = UsuariosController()

initialize()


@app.get('/healthz')
async def healthz():
  return controllers.healthz()

# FAMILIA

@app.post('/familia/create', tags=["Familia"])
async def create_familia(body: familiaModels.FamiliaRequest):
    return familia_controller.create_familia(body)


@app.get('/familia/get_all', tags=["Familia"])
async def get_all_familias():
    return familia_controller.get_all_familias()


@app.post('/familia/update', tags=["Familia"])
async def update_familia(body: familiaModels.FamiliaRequest, id: int):
    return familia_controller.update_familia(body, id)


@app.post('/familia/delete', tags=["Familia"])
async def delete_familia(id: int):
    return familia_controller.delete_familia(id)

# INQUILINO
@app.post('/inquilino/create', tags=["Inquilino"])
async def create_inquilino(body: inquilinoModels.InquilinoRequest):
    return inquilino_controller.create_inquilino(body)


@app.get('/inquilino/get_all', tags=["Inquilino"])
async def get_all_inquilinos():
    return inquilino_controller.get_all_inquilinos()


@app.post('/inquilino/update' , tags=["Inquilino"])
async def update_inquilino(body: inquilinoModels.InquilinoRequest, id: int):
    return inquilino_controller.update_inquilino(body, id)


@app.post('/inquilino/delete' , tags=["Inquilino"])
async def delete_inquilino(id: int):
    return inquilino_controller.delete_inquilino(id)

@app.post('/inquilino/marcar_fallecido', tags=["Inquilino"])
async def marcar_fallecido(id: int, fecha_muerte: Optional[datetime] = None):
    if not fecha_muerte:
        fecha_muerte = datetime.now()
    result = inquilino_controller.marcar_como_fallecido(id, fecha_muerte)
    return result

@app.get('/estancia/consultar_disponibilidad', tags=["Estancia"])
async def consultar_disponibilidad(estancia_id: int):
    result = inquilino_controller.consultardisponibilidad(estancia_id)
    return result

@app.post('/inquilino/asignar_estancia', tags=["Inquilino"])
async def asignar_estancia(inquilino_id: int, estancia_id: int):
    result = inquilino_controller.asignar_estancia(inquilino_id, estancia_id)
    return result
    
#ESTANCIA
@app.post('/estancia/create', tags=["Estancia"])
async def create_estancia(body: estanciaModels.EstanciaRequest):
    return estancia_controller.create_estancia(body)


@app.get('/estancia/get_all', tags=["Estancia"])
async def get_all_estancias():
    return estancia_controller.get_all_estancias()


@app.post('/estancia/update', tags=["Estancia"])
async def update_estancia(body: estanciaModels.EstanciaRequest, id: int):
    return estancia_controller.update_estancia(body, id)


@app.post('/estancia/delete', tags=["Estancia"])
async def delete_estancia(id: int):
    return estancia_controller.delete_estancia(id)

#EMPLEO
@app.post('/empleo/create', tags=["Empleo"])
async def create_empleo(body: empleoModels.EmpleoRequest):
    return empleo_controller.create_empleo(body)


@app.get('/empleo/get_all', summary="Get All Empleos", description="Retrieves all Empleo records from the database.", tags=["Empleo"])
async def get_all_empleos():
    return empleo_controller.get_all_empleos()


@app.post('/empleo/update', tags=["Empleo"])
async def update_empleo(body: empleoModels.EmpleoRequest, id: int):
    return empleo_controller.update_empleo(body, id)


@app.post('/empleo/delete', tags=["Empleo"])
async def delete_empleo(id: int):
    return empleo_controller.delete_empleo(id)

#RECURSOS
@app.post('/recurso/create', tags=["Recurso"])
async def create_recurso(body: recursoModels.RecursoRequest):
    return recurso_controller.create_recurso(body)


@app.get('/recurso/get_all', tags=["Recurso"])
async def get_all_recursos():
    return recurso_controller.get_all_recursos()


@app.post('/recurso/update', tags=["Recurso"])
async def update_recurso(body: recursoModels.RecursoRequest, id: int):
    return recurso_controller.update_recurso(body, id)


@app.post('/recurso/delete' , tags=["Recurso"])
async def delete_recurso(id: int):
    return recurso_controller.delete_recurso(id)

@app.get("/recurso/{id}/status" , tags=["Recurso"])
def get_recurso_status(id: int):
    result = recurso_controller.check_recurso_status(id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result
    
@app.post('/recurso/modify' , tags=["Recurso"])
async def modify_recurso(id: int, cantidad: int):
    result = recurso_controller.modify_recurso(id, cantidad)
    return result
#ROLES
@app.post('/roles/create' , tags=["Roles"])
async def create_role(body: rolesModels.RolesRequest):
    return roles_controller.create_role(body)


@app.get('/roles/get_all' , tags=["Roles"])
async def get_all_roles():
    return roles_controller.get_all_roles()


@app.post('/roles/update' , tags=["Roles"])
async def update_role(body: rolesModels.RolesRequest, id: int):
    return roles_controller.update_role(body, id)


@app.post('/roles/delete' , tags=["Roles"])
async def delete_role(id: int):
    return roles_controller.delete_role(id)

#USUARIOS
@app.post('/usuario/create' , tags=["Usuario"])
async def create_usuario(body: usuarioModels.UsuariosRequest):
    return usuario_controller.create_usuario(body)


@app.get('/usuarios/get_all' , tags=["Usuario"])
async def get_all_usuarios():
    return usuario_controller.get_all_usuarios()


@app.post('/usuarios/update' , tags=["Usuario"])
async def update_usuarios(body: usuarioModels.UsuariosRequest, id: int):
    return usuario_controller.update_usuario(body, id)

@app.post('/usuario/verify' , tags=["Usuario"])
async def verify_usuarios(usuario: str, password: str):
    return usuario_controller.verificar_usuario(usuario, password)


