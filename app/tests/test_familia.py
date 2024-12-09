import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

familia_id = None

# Test para crear familia
def test_create_familia():
    global familia_id
    # Datos de la familia para crear
    data = {"apellido": "Pérez"}
    
    response = client.post("/familia/create", json=data)
    
    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200  
    response_data = response.json()

# Test para obtener todas las familias
def test_get_all_familias():
    global familia_id
    response = client.get("/familia/get_all")
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

    # Actualizar los datos de la familia
    data = {"apellido": "González"}
    response = client.put(f"/familia/update/{familia_id}", json=data)

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

    # Eliminar la familia
    delete_response = client.post(f"/familia/delete?id={familia_id}")
    print("Delete response status code:", delete_response.status_code)
    print("Delete response JSON:", delete_response.json())

    # Verificar que la respuesta sea exitosa
    assert delete_response.status_code == 200

    # Comprobar que el estado de la respuesta sea "ok"
    assert delete_response.json().get("status") == "ok", "La familia no se eliminó correctamente"
