import pytest
from app.controllers.inquilino import InquilinoController
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

# Variable global para almacenar el ID del recurso
inquilino_id = None
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

def test_create_inquilino():
    global inquilino_id
    global auth_token
    auth_token = get_auth_token()
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post("/inquilino/create", json={
        "nombre": "InquilinoPrueba",
        "categoria": "CategoriaPrueba",
        "nacimiento": "1990-01-01",
        "muerte": "2024-01-01",
        "familia_id": 1,
        "empleo_id": 2,
        "roles_id": 1,
        "id_estancia": 2
    }, headers=headers)
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200


def test_get_all_inquilinos():
    global inquilino_id
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/inquilino/get_all", headers=headers)
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), list)
        
    # Perform a GET request to retrieve the ID of the inquilino named "InquilinoPrueba"
    inquilinos = response.json()
    inquilino_prueba = next((inquilino for inquilino in inquilinos if inquilino["nombre"] == "InquilinoPrueba"), None)
    assert inquilino_prueba is not None, "No se encontró el inquilino con nombre 'InquilinoPrueba'"
    inquilino_id = inquilino_prueba.get("id")


def test_update_inquilino():
    global inquilino_id
    # Asegurarse de que el inquilino se haya creado correctamente
    assert inquilino_id is not None, "El ID del inquilino no se obtuvo correctamente"

    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Actualizar el inquilino
    update_response = client.put(f"/inquilino/update/{inquilino_id}", json={
        "nombre": "InquilinoPruebaActualizado",
        "categoria": "CategoriaPruebaActualizada",
        "nacimiento": "1991-01-01",
        "muerte": "2025-01-01",
        "familia_id": 1,
        "empleo_id": 2,
        "roles_id": 1,
        "id_estancia": 2
    },headers=headers)
    print("Update response status code:", update_response.status_code)
    print("Update response JSON:", update_response.json())
    # Probar que la actualización fue exitosa
    assert update_response.status_code == 200
    assert update_response.json().get("status") == "ok"

def test_update_inquilino_notfound():
    inquilino_id = 999999
    # Asegurarse de que el inquilino se haya creado correctamente
    assert inquilino_id is not None, "El ID del inquilino no se obtuvo correctamente"

    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Actualizar el inquilino
    update_response = client.put(f"/inquilino/update/{inquilino_id}", json={
        "nombre": "InquilinoPruebaActualizado",
        "categoria": "CategoriaPruebaActualizada",
        "nacimiento": "1991-01-01",
        "muerte": "2025-01-01",
        "familia_id": 1,
        "empleo_id": 2,
        "roles_id": 1,
        "id_estancia": 2
    },headers=headers)
    print("Update response status code:", update_response.status_code)
    print("Update response JSON:", update_response.json())
    # Probar que la actualización fue exitosa
    assert update_response.status_code == 200
    assert update_response.json().get("error") == "Inquilino not found"

def test_marcarFallecido_inquilino():
    global inquilino_id
    # Asegurarse de que el inquilino se haya creado correctamente
    assert inquilino_id is not None, "El ID del inquilino no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}

    # Marcar al inquilino como fallecido
    params = {"id": inquilino_id}
    response = client.post(f"/inquilino/marcar_fallecido", params=params, headers=headers)
    assert response.status_code == 200
    assert response.json().get("status") == "Inquilino marcado como fallecido"

def test_marcarFallecido_inquilino_notfound():
    inquilino_id = 99999
    # Asegurarse de que el inquilino se haya creado correctamente
    assert inquilino_id is not None, "El ID del inquilino no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}

    # Marcar al inquilino como fallecido
    params = {"id": inquilino_id}
    response = client.post(f"/inquilino/marcar_fallecido",params=params, headers=headers)
    assert response.status_code == 200
    assert response.json().get("error") == "Inquilino no encontrado"

def test_delete_inquilino():
    global inquilino_id
    # Asegurarse de que el inquilino se haya creado correctamente
    assert inquilino_id is not None, "El ID del inquilino no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}

    # Eliminar el inquilino
    delete_response = client.delete(f"/inquilino/delete/{inquilino_id}", headers=headers)
    assert delete_response.status_code == 200
    assert delete_response.json().get("status") == "ok"

def test_delete_inquilino_notfound():
    inquilino_id = 999999
    # Asegurarse de que el inquilino se haya creado correctamente
    assert inquilino_id is not None, "El ID del inquilino no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}

    # Eliminar el inquilino
    delete_response = client.delete(f"/inquilino/delete/{inquilino_id}", headers=headers)
    assert delete_response.status_code == 200
    assert delete_response.json().get("error") == "Inquilino not found"
