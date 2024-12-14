import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

familia_id = None
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

# Test para crear familia
def test_create_familia():
    global familia_id
    global auth_token
    auth_token = get_auth_token()
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Datos de la familia para crear
    data = {"apellido": "Pérez"}
    
    response = client.post("/familia/create", json=data, headers=headers)
    
    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200  
    response_data = response.json()

# Test para obtener todas las familias
def test_get_all_familias():
    global familia_id
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/familia/get_all", headers=headers)
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
    # Realizar una solicitud GET para obtener el ID de la familia con apellido "Pérez"
    familias = response.json()
    familia_prueba = next((familia for familia in familias if familia["apellido"] == "Pérez"), None)
    assert familia_prueba is not None, "No se encontró la familia con apellido 'Pérez'"
    familia_id = familia_prueba.get("id")

def test_update_familia():
    global familia_id
    # Asegurarse de que el ID de la familia se haya creado correctamente
    assert familia_id is not None, "El ID de la familia no se obtuvo correctamente"

    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}

    # Actualizar los datos de la familia
    data = {"apellido": "González"}
    response = client.put(f"/familia/update/{familia_id}", json=data, headers=headers)

    # Verificar que la respuesta sea exitosa
    print("Update response status code:", response.status_code)
    print("Update response JSON:", response.json())
    assert response.status_code == 200

    # Usar get() para evitar KeyError y comprobar si la respuesta contiene la clave "status"
    response_data = response.json()
    status = response_data.get("status")

    if status == "ok":
        print(f"Familia con id {familia_id} actualizada correctamente.")
    else:
        print(f"Error al actualizar la familia con id {familia_id}: {response_data}")

    # Comprobar que la respuesta indica éxito
    assert status == "ok", f"Esperado 'ok', pero recibí: {status}"

def test_delete_familia():
    global familia_id
    # Asegurarse de que el ID de la familia se haya creado correctamente
    assert familia_id is not None, "El ID de la familia no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}

    # Eliminar la familia
    delete_response = client.post(f"/familia/delete?id={familia_id}", headers=headers)
    print("Delete response status code:", delete_response.status_code)
    print("Delete response JSON:", delete_response.json())

    # Verificar que la respuesta sea exitosa
    assert delete_response.status_code == 200

    # Comprobar que el estado de la respuesta sea "ok"
    assert delete_response.json().get("status") == "ok", "La familia no se eliminó correctamente"
