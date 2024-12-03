from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    """
    Test para el endpoint raíz.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "¡Hola, mundo!"}

def test_recursos_sin_pregunta():
    """
    Test para el endpoint /recursos sin pregunta.
    """
    response = client.get("/recursos")
    assert response.status_code == 200
    assert "recursos" in response.json()

def test_recursos_con_pregunta():
    """
    Test para el endpoint /recursos con una pregunta válida.
    """
    response = client.get("/recursos", params={"pregunta": "¿Qué asociaciones existen en Madrid?"})
    assert response.status_code == 200
    assert "pregunta" in response.json()
    assert "respuesta" in response.json()

def test_historia_sin_parametros():
    """
    Test para el endpoint /historia sin parámetros.
    """
    response = client.get("/historia")
    assert response.status_code == 200
    assert "articulos" in response.json()

def test_historia_con_opcion():
    """
    Test para el endpoint /historia con una opción válida.
    """
    response = client.get("/historia", params={"opcion": "Los disturbios de Stonewall"})
    assert response.status_code == 200
    assert "opcion" in response.json()
    assert "respuesta" in response.json()

def test_historia_con_consulta():
    """
    Test para el endpoint /historia con una consulta válida.
    """
    response = client.get("/historia", params={"consulta": "1969"})
    assert response.status_code == 200
    assert "consulta" in response.json()
    assert "respuesta" in response.json()

def test_formacion():
    """
    Test para el endpoint /formacion.
    """
    response = client.get("/formacion", params={"tema": "Cómo usar pronombres inclusivos"})
    assert response.status_code == 200
    assert "tema" in response.json()
    assert "respuesta" in response.json()
