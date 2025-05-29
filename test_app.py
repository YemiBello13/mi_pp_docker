import pytest
from app.main import app, una_funcion_simple # Importamos la app Flask y la función de main.py

# Pytest fixture para crear un cliente de prueba para la aplicación Flask
# Esto permite simular peticiones HTTP a tu aplicación sin levantar un servidor real.
@pytest.fixture
def client():
    # Configura la aplicación en modo de prueba
    app.config['TESTING'] = True
    with app.test_client() as client:
        # 'yield' hace que esto sea un generador, el cliente estará disponible
        # para las pruebas que lo usen, y cualquier limpieza se puede hacer después del yield.
        yield client

# Prueba para la página de inicio
def test_home_page(client):
    """Prueba que la página de inicio '/' carga correctamente y muestra el mensaje esperado."""
    response = client.get('/') # Simula una petición GET a la ruta '/'
    assert response.status_code == 200 # Verifica que el código de estado HTTP sea 200 (OK)
    # Verifica que el contenido esperado esté en la respuesta (b"" para bytes)
    assert b"Hola Mundo desde Docker y GitHub Actions!" in response.data

# Prueba para el endpoint de la API
def test_api_data(client):
    """Prueba que el endpoint '/api/data' devuelve los datos JSON esperados."""
    response = client.get('/api/data') # Simula una petición GET a la ruta '/api/data'
    assert response.status_code == 200 # Verifica el código de estado
    json_data = response.get_json() # obtiene los datos JSON de la respuesta
    assert json_data["name"] == "Dato de ejemplo" # Verifica un campo específico en el JSON
    assert json_data["status"] == "OK" # Verifica otro campo

# Pruebas para la función 'una_funcion_simple'
def test_una_funcion_simple_mayor():
    """Prueba una_funcion_simple cuando el primer argumento es mayor que el segundo."""
    assert una_funcion_simple(5, 3) == 2

def test_una_funcion_simple_menor_o_igual():
    """Prueba una_funcion_simple cuando el primer argumento es menor o igual que el segundo."""
    assert una_funcion_simple(3, 5) == 8
    assert una_funcion_simple(5, 5) == 10 # Cubriendo el caso 'else' a == b