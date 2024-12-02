import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

##DOCUMENTARRRRRRRRRR#######################
#TRY Y CATCH ES MUY IMPORTANTE
# 3 puntos: cobertura total, 
#   si existen y se pueden ejecutar (o se puede ejecutar en github actions y funcionan arriba)
#   Integración continua
#   test de integración --> Que se manden todas a la vez

# Variable global para almacenar el ID del recurso
rol_id = None

def test_create_role():
    global rol_id
    response = client.post("/role/create", json={
        "nombre": "RolePrueba"
    })
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert response.json().get("status") == "ok"

    # Obtener el ID del rol creado
    roles_response = client.get("/role/get_all")
    roles = roles_response.json()
    rol_prueba = next((rol for rol in roles if rol["nombre"] == "RolePrueba"), None)
    assert rol_prueba is not None, "No se encontró el rol con nombre 'RolePrueba'"
    role_id = rol_prueba.get("id")

def test_get_all_roles():
    global rol_id
    response = client.get("/role/get_all")
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), list)
        
    # Perform a GET request to retrieve the ID of the role named "RolePrueba"
    roles = response.json()
    role_prueba = next((rol for rol in roles if rol["nombre"] == "RolePrueba"), None)
    assert rol_prueba is not None, "No se encontró el rol con nombre 'RolePrueba'"
    rol_id = rol_prueba.get("id")