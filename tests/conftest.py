import pytest
import requests

@pytest.fixture
def url_base():
    return "https://jsonplaceholder.typicode.com/"

@pytest.fixture
def url_apuestas(url_base):
    return url_base + "posts/"

@pytest.fixture(scope="session")
def api():
    sesion = requests.Session()
    yield sesion
    sesion.close()
