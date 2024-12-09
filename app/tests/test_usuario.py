import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

# Variable global para almacenar el token de autenticación
auth_token = None
usuario_id = None

def test_create_usuario():
    global usuario_id, auth_token

    # Crear un nuevo usuario sin necesidad de autenticación
    response = client.post("/usuarios/create", json={
        "usuario": "UsuarioPrueba",
        "password": "123"
    })
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    usuario_id = response.json().get("id")
    assert usuario_id is not None, "El ID del usuario no se obtuvo correctamente"
    assert response.json().get("status") == "ok"

    # Obtener el token de autenticación para el usuario creado
    response = client.post("usuarios/verificar", data={"username": "UsuarioPrueba", "password": "123"})
    assert response.status_code == 200
    auth_token = response.json().get("access_token")
    assert auth_token is not None, "El token de autenticación no se obtuvo correctamente"

def test_verificar_usuarios():
    global usuario_id, auth_token
    # Asegurarse de que el usuario se haya creado correctamente
    assert usuario_id is not None, "El ID del usuario no se obtuvo correctamente"

    # Verificar el usuario con las credenciales correctas
    response = client.post("/usuarios/verificar", data={"username": "UsuarioPrueba", "password": "123"})
    assert response.status_code == 200

def test_get_all_usuarios():
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/usuarios/get_all", headers=headers)
    assert response.status_code == 200

def test_update_usuario():
    global usuario_id, auth_token
    assert usuario_id is not None, "El ID del usuario no se obtuvo correctamente"

    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post(f"/usuarios/update?id={usuario_id}", json={
        "usuario": "UsuarioPruebaActualizado",
        "password": "1234"
    }, headers=headers)
    assert response.status_code == 200

def test_delete_usuario():
    global usuario_id, auth_token
    assert usuario_id is not None, "El ID del usuario no se obtuvo correctamente"

    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post(f"/usuarios/delete?id={usuario_id}", headers=headers)
    assert response.status_code == 200

