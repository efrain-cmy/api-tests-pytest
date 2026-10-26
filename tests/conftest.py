import pytest
import requests

@pytest.fixture
def url_base():
    return "https://jsonplaceholder.typicode.com/"

@pytest.fixture(scope="session")
def api():
    sesion = requests.Session()
    yield sesion
    sesion.close()