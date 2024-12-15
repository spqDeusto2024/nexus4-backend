import pytest
from app.main import app
from fastapi.testclient import TestClient
client = TestClient(app)

estancia_id = None
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

#TESTS ESTANCIA
def test_create_estancia():
    auth_token = get_auth_token()
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post("/estancia/create", json={
        "nombre": "EstanciaPrueba",
        "categoria": "CategoriaPrueba",
        "personas_actuales": 5,
        "capacidad_max": 20,
        "recurso_id": 1  # Asegúrate de que este recurso_id exista en tu base de datos
    },headers=headers)
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200

def test_get_all_estancias():
    global estancia_id
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/estancia/get_all", headers=headers)
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), list)
        
    # Perform a GET request to retrieve the ID of the estancia named "EstanciaPrueba"
    estancias = response.json()
    estancia_prueba = next((estancia for estancia in estancias if estancia["nombre"] == "EstanciaPrueba"), None)
    assert estancia_prueba is not None, "No se encontró la estancia con nombre 'EstanciaPrueba'"
    estancia_id = estancia_prueba.get("id")

def test_update_estancia():
    global estancia_id
    # Asegurarse de que la estancia se haya creado correctamente
    assert estancia_id is not None, "El ID de la estancia no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Actualizar la estancia con datos válidos
    update_response = client.put(f"/estancia/update/{estancia_id}", json={
        "nombre": "EstanciaPruebaActualizada",
        "categoria": "CategoriaActualizada",
        "personas_actuales": 10,
        "capacidad_max": 30,
        "recurso_id": 1  # Asegúrate de que este recurso_id exista en tu base de datos
    }, headers=headers)
    print("Update response status code:", update_response.status_code)
    print("Update response JSON:", update_response.json())
    assert update_response.status_code == 200
    assert update_response.json().get("status") == "ok"

def test_update_estancia_not_found():
    estancia_id = 999999
    # Asegurarse de que la estancia se haya creado correctamente
    assert estancia_id is not None, "El ID de la estancia no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Actualizar la estancia con datos válidos
    update_response = client.put(f"/estancia/update/{estancia_id}", json={
        "nombre": "EstanciaPruebaActualizada",
        "categoria": "CategoriaActualizada",
        "personas_actuales": 10,
        "capacidad_max": 30,
        "recurso_id": 1  # Asegúrate de que este recurso_id exista en tu base de datos
    }, headers=headers)
    print("Update response status code:", update_response.status_code)
    print("Update response JSON:", update_response.json())
    assert update_response.status_code == 200
    assert update_response.json().get("error") == "Estancia not found", "El mensaje de error no es el esperado"

"""
def test_consultar_disponibilidad():
    global estancia_id
    print("Estancia ID:", estancia_id)  
    assert estancia_id is not None, "El ID de la estancia no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get(f"/estancia/consultar_disponibilidad?estancia_id={estancia_id}", headers=headers)
    assert response.status_code == 200
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.json().get("status") == "ok"
"""

def test_asignar_estancia():
    global estancia_id
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post(
        "/inquilino/asignar_estancia",
        params={"inquilino_id": 2, "estancia_id": estancia_id}  # Enviar parámetros en la URL
        , headers=headers)
    assert response.status_code == 200

def test_asignar_estancia_notfound():
    estancia_id = 999999
    # Asegurarse de que la estancia se haya creado correctamente
    assert estancia_id is not None, "El ID de la estancia no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Eliminar la estancia
    response = client.post(
        "/inquilino/asignar_estancia",
        params={"inquilino_id": 2, "estancia_id": estancia_id}  # Enviar parámetros en la URL
        , headers=headers)

    assert response.status_code == 200
    assert response.json().get("error") == "Estancia no encontrada", "El mensaje de error no es el esperado"

def test_detele_estancia():
    global estancia
    # Asegurarse de que el ID de la estancia se haya creado correctamente
    assert estancia_id is not None, "El ID de la estancia no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}

    # Eliminar la estancia
    delete_response = client.delete(f"/estancia/delete/{estancia_id}", headers=headers)
    print("Delete response status code:", delete_response.status_code)
    print("Delete response JSON:", delete_response.json())

    # Verificar que la respuesta sea exitosa
    assert delete_response.status_code == 200

    # Comprobar que el estado de la respuesta sea "ok"
    assert delete_response.json().get("status") == "ok", "La estancia no se eliminó correctamente"

def test_delete_estancia_notfound():
    estancia_id = 999999
    # Asegurarse de que la estancia se haya creado correctamente
    assert estancia_id is not None, "El ID de la estancia no se obtuvo correctamente"
    global auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    # Eliminar la estancia
    delete_response = client.delete(f"/estancia/delete/{estancia_id}", headers=headers)
    print("Delete response status code:", delete_response.status_code)
    print("Delete response JSON:", delete_response.json())

    assert delete_response.status_code == 200
    assert delete_response.json().get("error") == "Estancia not found", "El mensaje de error no es el esperado"
