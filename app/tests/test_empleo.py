import pytest
from fastapi.testclient import TestClient
from app.main import app
from fastapi import HTTPException, status

client = TestClient(app)

empleo_id = None
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

# Test para crear empleo
def test_create_empleo():
    global empleo_id
    global auth_token
    auth_token = get_auth_token()
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Datos del empleo para crear
    data = {"empleo": "Picador", "edad_minima": 18, "id_estancia": 1}
    
    response = client.post("/empleo/create", json=data, headers=headers)
    
    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200  
    response_data = response.json()

# Test para obtener todos los empleos
def test_get_all_empleos():
    global empleo_id
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/empleo/get_all", headers=headers)
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    
    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
    # Realizar una solicitud GET para obtener el ID del empleo con nombre "Programador"
    empleos = response.json()
    empleo_prueba = next((empleo for empleo in empleos if empleo["empleo"] == "Picador"), None)
    assert empleo_prueba is not None, "No se encontró el empleo con nombre 'Picador'"
    empleo_id = empleo_prueba.get("id")

# Test para actualizar empleo
def test_update_empleo():
    global empleo_id
    # Asegurarse de que el ID del empleo se haya creado correctamente
    assert empleo_id is not None, "El ID del empleo no se obtuvo correctamente"

    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}

    # Actualizar los datos del empleo
    data = {"empleo": "Desarrollador", "edad_minima": 21, "id_estancia": 1}
    response = client.put(f"/empleo/update/{empleo_id}", json=data, headers=headers)

    # Verificar que la respuesta sea exitosa
    print("Update response status code:", response.status_code)
    print("Update response JSON:", response.json())
    assert response.status_code == 200

    # Usar get() para evitar KeyError y comprobar si la respuesta contiene la clave "status"
    response_data = response.json()
    status = response_data.get("status")

    if status == "ok":
        print(f"Empleo con id {empleo_id} actualizado correctamente.")
    else:
        print(f"Error al actualizar el empleo con id {empleo_id}: {response_data}")

    # Comprobar que la respuesta indica éxito
    assert status == "ok", f"Esperado 'ok', pero recibí: {status}"

# Test para eliminar empleo
def test_delete_empleo():
    global empleo_id
    # Asegurarse de que el ID del empleo se haya creado correctamente
    assert empleo_id is not None, "El ID del empleo no se obtuvo correctamente"

    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}

    # Eliminar el empleo
    delete_response = client.delete(f"/empleo/delete/{empleo_id}", headers=headers)
    print("Delete response status code:", delete_response.status_code)
    print("Delete response JSON:", delete_response.json())

    # Verificar que la respuesta sea exitosa
    assert delete_response.status_code == 200

    # Comprobar que el estado de la respuesta sea "ok"
    assert delete_response.json().get("status") == "ok", "El empleo no se eliminó correctamente"