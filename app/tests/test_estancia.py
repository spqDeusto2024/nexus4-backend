import pytest
from app.main import app
from fastapi.testclient import TestClient
client = TestClient(app)

estancia_id = None

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
    update_response = client.post(f"/estancia/update?id={estancia_id}", json={
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

def test_consultar_disponibilidad():
    global estancia_id
    # Asegurarse de que la estancia se haya creado correctamente
    assert estancia_id is not None, "El ID de la estancia no se obtuvo correctamente"

    try:
        # Consultar disponibilidad con un número de personas que debería estar disponible
        disponibilidad_response = client.get(f"/estancia/consultar_disponibilidad?estancia_id={estancia_id}&numero_personas=5")
        print("Disponibilidad response status code:", disponibilidad_response.status_code)
        print("Disponibilidad response JSON:", disponibilidad_response.json())
        assert disponibilidad_response.status_code == 200
        assert disponibilidad_response.json().get("disponible") is True

        # Consultar disponibilidad con un número de personas que debería no estar disponible
        # Asegúrate de que el número de personas actuales en la estancia más el número de personas consultadas exceda la capacidad máxima
        estancia_response = client.get(f"/estancia/get_all")
        estancias = estancia_response.json()
        estancia_prueba = next((estancia for estancia in estancias if estancia["id"] == estancia_id), None)
        assert estancia_prueba is not None, "No se encontró la estancia con el ID proporcionado"
        personas_actuales = estancia_prueba["personas_actuales"]
        capacidad_max = estancia_prueba["capacidad_max"]

        numero_personas = capacidad_max - personas_actuales + 1  # Esto debería exceder la capacidad máxima

        no_disponibilidad_response = client.get(f"/estancia/consultar_disponibilidad?estancia_id={estancia_id}&numero_personas={numero_personas}")
        print("No disponibilidad response status code:", no_disponibilidad_response.status_code)
        print("No disponibilidad response JSON:", no_disponibilidad_response.json())
        assert no_disponibilidad_response.status_code == 200
        assert no_disponibilidad_response.json().get("disponible") is False

    except Exception as e:
        print(f"An error occurred: {e}")
        assert False, f"Test failed due to an unexpected error: {e}"

def test_asignar_estancia():
    global estancia_id
    global inquilino_id

    # Asegurarse de que la estancia y el inquilino se hayan creado correctamente
    assert estancia_id is not None, "El ID de la estancia no se obtuvo correctamente"
    assert inquilino_id is not None, "El ID del inquilino no se obtuvo correctamente"

    try:
        # Asignar la estancia al inquilino
        asignar_response = client.post(f"/inquilino/asignar_estancia?inquilino_id={inquilino_id}&estancia_id={estancia_id}")
        print("Asignar response status code:", asignar_response.status_code)
        print("Asignar response JSON:", asignar_response.json())
        assert asignar_response.status_code == 200
        assert asignar_response.json().get("status") == "Estancia asignada exitosamente"

        # Intentar asignar la estancia nuevamente al mismo inquilino para verificar la capacidad máxima
        asignar_response_max = client.post(f"/inquilino/asignar_estancia?inquilino_id={inquilino_id}&estancia_id={estancia_id}")
        print("Asignar response max status code:", asignar_response_max.status_code)
        print("Asignar response max JSON:", asignar_response_max.json())
        assert asignar_response_max.status_code == 200
        assert asignar_response_max.json().get("error") == "La capacidad máxima de la estancia ha sido alcanzada"

    except Exception as e:
        print(f"An error occurred: {e}")
        assert False, f"Test failed due to an unexpected error: {e}"

def test_delete_estancia():
    global estancia_id
    # Asegurarse de que la estancia se haya creado correctamente
    assert estancia_id is not None, "El ID de la estancia no se obtuvo correctamente"

    # Eliminar la estancia
    delete_response = client.post(f"/estancia/delete?id={estancia_id}")
    print("Delete response status code:", delete_response.status_code)
    print("Delete response JSON:", delete_response.json())
    assert delete_response.status_code == 200
    assert delete_response.json().get("status") == "ok"