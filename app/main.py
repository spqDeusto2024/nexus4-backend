from fastapi import FastAPI
from typing import Union
from app.controllers import (
    FamiliaController,
    InquilinoController,
    EstanciaController,
    EmpleoController,
    RecursoController,
    RolesController,
)
from app.mysql.mysql import DatabaseClient

import app.utils.vars as gb
import app.models.models as models


def initialize() -> None:
  # initialize database
  dbClient = DatabaseClient(gb.MYSQL_URL)
  dbClient.init_database()
  return


app = FastAPI()
controllers = Controllers()

initialize()


@app.get('/healthz')
async def healthz():
  return controllers.healthz()

# FAMILIA
@app.post('/familia/create')
async def create_familia(body: models.FamiliaRequest):
    return FamiliaController.create_familia(body)


@app.get('/familia/get_all')
async def get_all_familias():
    return FamiliaController.get_all_familias()


@app.post('/familia/update')
async def update_familia(body: models.FamiliaRequest, id: int):
    return FamiliaController.update_familia(body, id)


@app.post('/familia/delete')
async def delete_familia(id: int):
    return FamiliaController.delete_familia(id)

# INQUILINO
@app.post('/inquilino/create')
async def create_inquilino(body: models.InquilinoRequest):
    return InquilinoController.create_inquilino(body)


@app.get('/inquilino/get_all')
async def get_all_inquilinos():
    return InquilinoController.get_all_inquilinos()


@app.post('/inquilino/update')
async def update_inquilino(body: models.InquilinoRequest, id: int):
    return InquilinoController.update_inquilino(body, id)


@app.post('/inquilino/delete')
async def delete_inquilino(id: int):
    return InquilinoController.delete_inquilino(id)

#ESTANCIA
@app.post('/estancia/create')
async def create_estancia(body: models.EstanciaRequest):
    return EstanciaController.create_estancia(body)


@app.get('/estancia/get_all')
async def get_all_estancias():
    return EstanciaController.get_all_estancias()


@app.post('/estancia/update')
async def update_estancia(body: models.EstanciaRequest, id: int):
    return EstanciaController.update_estancia(body, id)


@app.post('/estancia/delete')
async def delete_estancia(id: int):
    return EstanciaController.delete_estancia(id)

#EMPLEO
@app.post('/empleo/create')
async def create_empleo(body: models.EmpleoRequest):
    return EmpleoController.create_empleo(body)


@app.get('/empleo/get_all')
async def get_all_empleos():
    return EmpleoController.get_all_empleos()


@app.post('/empleo/update')
async def update_empleo(body: models.EmpleoRequest, id: int):
    return EmpleoController.update_empleo(body, id)


@app.post('/empleo/delete')
async def delete_empleo(id: int):
    return EmpleoController.delete_empleo(id)

#RECURSOS
@app.post('/recurso/create')
async def create_recurso(body: models.RecursoRequest):
    return RecursoController.create_recurso(body)


@app.get('/recurso/get_all')
async def get_all_recursos():
    return RecursoController.get_all_recursos()


@app.post('/recurso/update')
async def update_recurso(body: models.RecursoRequest, id: int):
    return RecursoController.update_recurso(body, id)


@app.post('/recurso/delete')
async def delete_recurso(id: int):
    return RecursoController.delete_recurso(id)

#ROLES
@app.post('/roles/create')
async def create_role(body: models.RolesRequest):
    return RolesController.create_role(body)


@app.get('/roles/get_all')
async def get_all_roles():
    return RolesController.get_all_roles()


@app.post('/roles/update')
async def update_role(body: models.RolesRequest, id: int):
    return RolesController.update_role(body, id)


@app.post('/roles/delete')
async def delete_role(id: int):
    return RolesController.delete_role(id)


# @app.post('/user/create')
# def createUser():
