import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

# Variable global para almacenar el ID del recurso
role_id = None
auth_token = None

def get_auth_token():
    global auth_token
    if auth_token is not None:
        return auth_token

    # Crear un nuevo usuario sin necesidad de autenticación
    response = client.post("/usuarios/create", json={
        "usuario": "UsuarioPrueba",
        "password": "123"
    })
    assert response.status_code == 200
    assert response.json().get("status") == "ok"

    # Obtener el token de autenticación para el usuario creado
    response = client.post("usuarios/verificar", data={"username": "UsuarioPrueba", "password": "123"})
    assert response.status_code == 200
    auth_token = response.json().get("access_token")
    assert auth_token is not None, "El token de autenticación no se obtuvo correctamente"

    return auth_token

def test_create_role():
    global role_id
    global auth_token
    auth_token = get_auth_token()
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post("/roles/create", json={
        "nombre": "RolePrueba"
    }, headers=headers)
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert response.json().get("status") == "ok"

        

def test_get_all_roles():
    global role_id
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/roles/get_all", headers=headers)
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), list)
        
    # Perform a GET request to retrieve the ID of the role named "RolePrueba"
    roles = response.json()
    role_prueba = next((role for role in roles if role["nombre"] == "RolePrueba"), None)
    assert role_prueba is not None, "No se encontró el rol con nombre 'RolePrueba'"
    role_id = role_prueba.get("id")

def test_update_role():
    global role_id
    # Asegurarse de que el rol se haya creado correctamente
    assert role_id is not None, "El ID del rol no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    
    # Actualizar el rol con datos válidos
    update_response = client.put(f"/roles/update/{role_id}", json={
        "nombre": "RolePruebaActualizado",
    }, headers=headers) 
    print("Update response status code:", update_response.status_code)
    print("Update response JSON:", update_response.json())
    assert update_response.status_code == 200
    assert update_response.json().get("status") == "ok"

def test_delete_role():
    global role_id
    # Asegurarse de que el rol se haya creado correctamente
    assert role_id is not None, "El ID del rol no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Eliminar el rol
    delete_response = client.delete(f"/roles/delete/{role_id}", headers=headers)
    print("Delete response status code:", delete_response.status_code)
    print("Delete response JSON:", delete_response.json())
    assert delete_response.status_code == 200
    assert delete_response.json().get("status") == "ok"