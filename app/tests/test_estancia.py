import pytest
from app.main import app
from fastapi.testclient import TestClient
client = TestClient(app)

estancia_id = None
inquilino_id = None

#TESTS ESTANCIA
def test_create_estancia():
    response = client.post("/estancia/create", json={
        "nombre": "EstanciaPrueba",
        "categoria": "CategoriaPrueba",
        "personas_actuales": 5,
        "capacidad_max": 20,
        "recurso_id": 1  # Asegúrate de que este recurso_id exista en tu base de datos
    })
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200

def test_get_all_estancias():
    global estancia_id
    response = client.get("/estancia/get_all")
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

    # Actualizar la estancia con datos válidos
    update_response = client.put(f"/estancia/update/{estancia_id}", json={
        "nombre": "EstanciaPruebaActualizada",
        "categoria": "CategoriaActualizada",
        "personas_actuales": 10,
        "capacidad_max": 30,
        "recurso_id": 1  # Asegúrate de que este recurso_id exista en tu base de datos
    })
    print("Update response status code:", update_response.status_code)
    print("Update response JSON:", update_response.json())
    assert update_response.status_code == 200
    assert update_response.json().get("status") == "ok"
"""
def test_consultar_disponibilidad():
    global estancia_id
    assert estancia_id is not None, "El ID de la estancia no se obtuvo correctamente"

    # Consulta disponibilidad sin `numero_personas`
    disponibilidad_response = client.get(f"/estancia/consultar_disponibilidad?estancia_id={estancia_id}")
    print("Disponibilidad response status code:", disponibilidad_response.status_code)
    print("Disponibilidad response JSON:", disponibilidad_response.json())
    assert disponibilidad_response.status_code == 200

    # Verifica que el JSON tenga el campo esperado
    respuesta = disponibilidad_response.json()
    assert "disponible" in respuesta, "El campo 'disponible' no está en la respuesta"
    assert isinstance(respuesta["disponible"], bool), "'disponible' debe ser un booleano"


def test_asignar_estancia():
    global estancia_id, inquilino_id

    # Crear un inquilino para realizar el test
    inquilino_response = client.post("/inquilino/create", json={
        "nombre": "InquilinoPrueba",
        "apellido": "ApellidoPrueba",
        "edad": 30,
        "dni": "12345678A",  
        "categoria": "PruebaCategoria",  
        "familia_id": 1,  
        "empleo_id": 1,   
        "roles_id": 1  
    })
    print("Inquilino response status code:", inquilino_response.status_code)
    print("Inquilino response JSON:", inquilino_response.json())
    assert inquilino_response.status_code == 200

    # Obtener el ID del inquilino creado
    inquilino_data = inquilino_response.json()
    inquilino_id = inquilino_data.get("id")
    assert inquilino_id is not None, "El ID del inquilino no se obtuvo correctamente"

    # Asignar la estancia al inquilino
    asignar_response = client.post(f"/estancia/asignar_estancia?inquilino_id={inquilino_id}&estancia_id={estancia_id}")
    print("Asignar response status code:", asignar_response.status_code)
    print("Asignar response JSON:", asignar_response.json())
    assert asignar_response.status_code == 200

    # Verificar el estado de la respuesta
    asignar_status = asignar_response.json().get("status")
    assert asignar_status == "Estancia asignada exitosamente", "La asignación no se completó correctamente"
    """