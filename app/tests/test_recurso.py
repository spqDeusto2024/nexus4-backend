import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)
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

def test_create_recurso():
    global recurso_id
    global auth_token
    auth_token = get_auth_token()
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post("/recurso/create", json={"nombre": "RecursoPrueba", "capacidad_min": 10, "capacidad_max": 100, "capacidad_actual": 50}, headers=headers)
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200

def test_get_all_recursos():
    global recurso_id
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/recurso/get_all",headers=headers)
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), list)
        
    # Perform a GET request to retrieve the ID of the resource named "RecursoPrueba"
    recursos = response.json()
    recurso_prueba = next((recurso for recurso in recursos if recurso["nombre"] == "RecursoPrueba"), None)
    assert recurso_prueba is not None, "No se encontró el recurso con nombre 'RecursoPrueba'"
    recurso_id = recurso_prueba.get("id")

# Un test tiene que ejecutar todos los supuestos o la mayoría HAY QUE HACER CON TRY y CATCH y forzar si funciona o no funciona
def test_update_recurso():
    global recurso_id
    # Asegurarse de que el recurso se haya creado correctamente
    assert recurso_id is not None, "El ID del recurso no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Actualizar el recurso
    update_response = client.put(f"/recurso/update/{recurso_id}", json={"nombre": "RecursoPrueba", "capacidad_min": 5, "capacidad_max": 100, "capacidad_actual": 50},headers=headers)
    print("Update response status code:", update_response.status_code)
    print("Update response JSON:", update_response.json())
    #Puedo probar que un assert sea falso. Cuanto más probado está mejor. Pasar una función para algo que no se puede insertar.
    #Hay que probar una que funcione y una que no.
    assert update_response.status_code == 200
    assert update_response.json().get("status") == "ok"

def test_get_recurso_status():
    global recurso_id
    # Asegurarse de que el recurso se haya creado correctamente
    assert recurso_id is not None, "El ID del recurso no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Obtener el estado del recurso
    status_response = client.get(f"/recurso/{recurso_id}/status", headers=headers)
    assert status_response.status_code == 200
    assert status_response.json().get("status") in ["ok", "alert"]

def test_delete_recurso():
    global recurso_id
    # Asegurarse de que el recurso se haya creado correctamente
    assert recurso_id is not None, "El ID del recurso no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Eliminar el recurso
    delete_response = client.delete(f"/recurso/delete/{recurso_id}",headers=headers)
    assert delete_response.status_code == 200
    assert delete_response.json().get("status") == "ok"
