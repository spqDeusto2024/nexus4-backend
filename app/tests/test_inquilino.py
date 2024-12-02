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
inquilino_id = None

#TESTS INQUILINOS

def test_create_inquilino():
    global inquilino_id
    response = client.post("/inquilino/create", json={
        "nombre": "InquilinoPrueba",
        "categoria": "CategoriaPrueba",
        "nacimiento": "1990-01-01",
        "muerte": "2024-01-01",
        "familia_id": 1,
        "empleo_id": 2,
        "roles_id": 1,
        "id_estancia": 2
    })
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200


def test_get_all_inquilinos():
    global inquilino_id
    response = client.get("/inquilino/get_all")
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

    # Actualizar el inquilino
    update_response = client.post(f"/inquilino/update?id={inquilino_id}", json={
        "nombre": "InquilinoPruebaActualizado",
        "categoria": "CategoriaPruebaActualizada",
        "nacimiento": "1991-01-01",
        "muerte": "2025-01-01",
        "familia_id": 1,
        "empleo_id": 2,
        "roles_id": 1,
        "id_estancia": 2
    })
    print("Update response status code:", update_response.status_code)
    print("Update response JSON:", update_response.json())
    # Probar que la actualización fue exitosa
    assert update_response.status_code == 200
    assert update_response.json().get("status") == "ok"


def test_delete_inquilino():
    global inquilino_id
    # Asegurarse de que el inquilino se haya creado correctamente
    assert inquilino_id is not None, "El ID del inquilino no se obtuvo correctamente"

    # Eliminar el inquilino
    delete_response = client.post(f"/inquilino/delete?id={inquilino_id}")
    assert delete_response.status_code == 200
    assert delete_response.json().get("status") == "ok"
