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
role_id = None

def test_create_role():
    global role_id
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
    global role_id
    response = client.get("/role/get_all")
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), list)
        
    # Perform a GET request to retrieve the ID of the role named "RolePrueba"
    roles = response.json()
    role_prueba = next((rol for role in roles if role["nombre"] == "RolePrueba"), None)
    assert role_prueba is not None, "No se encontró el rol con nombre 'RolePrueba'"
    role_id = role_prueba.get("id")

def test_update_role():
    global role_id
    # Asegurarse de que el rol se haya creado correctamente
    assert role_id is not None, "El ID del rol no se obtuvo correctamente"

    
    # Actualizar el rol con datos válidos
        update_response = client.post(f"/role/update?id={role_id}", json={
            "nombre": "RolePruebaActualizado",
        })
        print("Update response status code:", update_response.status_code)
        print("Update response JSON:", update_response.json())
        assert update_response.status_code == 200
        assert update_response.json().get("status") == "ok"

def test_delete_role():
    global role_id
    # Asegurarse de que el rol se haya creado correctamente
    assert role_id is not None, "El ID del rol no se obtuvo correctamente"

    # Eliminar el rol
    delete_response = client.post(f"/role/delete?id={role_id}")
    print("Delete response status code:", delete_response.status_code)
    print("Delete response JSON:", delete_response.json())
    assert delete_response.status_code == 200
    assert delete_response.json().get("status") == "ok"