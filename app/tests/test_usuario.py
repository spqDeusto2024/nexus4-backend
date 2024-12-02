import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_usuario():
    global usuario_id
    response = client.post("/usuarios/create", json={
        "usuario": "UsuarioPrueba",
        "password": "123"
    })
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_all_usuarios():
    global usuario_id
    response = client.get("/usuario/get_all")
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), list)
        
    # Perform a GET request to retrieve the ID of the usuario named "UsuarioPrueba"
    usuarios = response.json()
    usuario_prueba = next((usuario for usuario in usuarios if usuario["usuario"] == "UsuarioPrueba"), None)
    assert usuario_prueba is not None, "No se encontró el usuario con nombre 'UsuarioPrueba'"
    usuario_id = usuario_prueba.get("id")
    assert usuario_id is not None, "El ID del usuario no se obtuvo correctamente"

def test_update_usuario():
    global usuario_id
    # Asegurarse de que el usuario se haya creado correctamente
    assert usuario_id is not None, "El ID del usuario no se obtuvo correctamente"

    # Actualizar el usuario
    update_response = client.post(f"/usuarios/update?id={usuario_id}", json={
        "usuario": "UsuarioPrueba",
        "password": "123"
    })
    print("Update response status code:", update_response.status_code)
    print("Update response JSON:", update_response.json())
    assert update_response.status_code == 200
    assert update_response.json().get("status") == "ok"

def test_verificar_usuarios():
    global usuario_id
    # Asegurarse de que el usuario se haya creado correctamente
    assert usuario_id is not None, "El ID del usuario no se obtuvo correctamente"

    # Verificar el usuario con las credenciales correctas
    response = client.post("/usuarios/verificar", data={
        "username": "UsuarioPrueba",
        "password": "123"
    })
    print("Verify response status code:", response.status_code)
    print("Verify response JSON:", response.json())
    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"

    # Verificar el usuario con una contraseña incorrecta
    response = client.post("/usuarios/verificar", data={
        "username": "UsuarioPrueba",
        "password": "incorrecta"
    })
    print("Verify incorrect password response status code:", response.status_code)
    print("Verify incorrect password response JSON:", response.json())
    assert response.status_code == 401
    assert response.json()["detail"] == "Contraseña incorrecta"

    # Verificar un usuario que no existe
    response = client.post("/usuarios/verificar", data={
        "username": "UsuarioNoExistente",
        "password": "123"
    })
    print("Verify non-existent user response status code:", response.status_code)
    print("Verify non-existent user response JSON:", response.json())
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuario no encontrado"

def test_delete_usuario():
    global usuario_id
    # Asegurarse de que el usuario se haya creado correctamente
    assert usuario_id is not None, "El ID del usuario no se obtuvo correctamente"

    # Eliminar el usuario
    delete_response = client.post(f"/usuario/delete?id={usuario_id}")
    assert delete_response.status_code == 200
    assert delete_response.json().get("status") == "ok"

