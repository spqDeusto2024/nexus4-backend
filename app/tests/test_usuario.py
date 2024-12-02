import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Variable global para almacenar el ID del usuario
usuario_id = None

def test_create_usuario():
    global usuario_id
    response = client.post("/usuarios/create", json={"usuario": "UsuarioPrueba", "password": "password123"})
    assert response.status_code == 200
    usuario_id = response.json().get("id")
    assert usuario_id is not None, "El ID del usuario no se obtuvo correctamente"

def test_verificar_usuarios():
    global usuario_id
    # Asegurarse de que el usuario se haya creado correctamente
    assert usuario_id is not None, "El ID del usuario no se obtuvo correctamente"

    # Verificar el usuario
    response = client.post("/usuarios/verificar", json={"usuario": "UsuarioPrueba", "password": "password123"})
    assert response.status_code == 200
    data = response.json()
    assert data["usuario"] == "UsuarioPrueba"
    assert "id" in data

def test_verificar_usuarios_incorrecto():
    # Verificar el usuario con contraseña incorrecta
    response = client.post("/usuarios/verificar", json={"usuario": "UsuarioPrueba", "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Contraseña incorrecta"

def test_verificar_usuarios_no_existente():
    # Verificar un usuario que no existe
    response = client.post("/usuarios/verificar", json={"usuario": "UsuarioNoExistente", "password": "password123"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuario no encontrado"
    client = TestClient(app)

def test_update_usuario():
    global usuario_id
    # Asegurarse de que el usuario se haya creado correctamente
    assert usuario_id is not None, "El ID del usuario no se obtuvo correctamente"

    # Actualizar el usuario
    response = client.put(f"/usuarios/{usuario_id}", json={"usuario": "UsuarioPruebaActualizado", "password": "password123"})
    assert response.status_code == 200
    data = response.json()
    assert data["usuario"] == "UsuarioPruebaActualizado"

def test_delete_usuario():
    global usuario_id
    # Asegurarse de que el usuario se haya creado correctamente
    assert usuario_id is not None, "El ID del usuario no se obtuvo correctamente"

    # Eliminar el usuario
    response = client.delete(f"/usuarios/{usuario_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Usuario eliminado correctamente"

    # Verificar que el usuario ya no existe
    response = client.post("/usuarios/verificar", json={"usuario": "UsuarioPruebaActualizado", "password": "password123"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuario no encontrado"