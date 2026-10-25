
import pytest
import requests

def test_apuestas_devuelve_201_y_ticket_con_id(url_base):
    #arrange-url base
    url = url_base + "posts"
    apuesta = {"partido": "Real Madrid vs Barça", "monto": 50}
    #act-mandar una petición post
    respuesta  = requests.post(url, json=apuesta, timeout=10)
    #assert-validar status,monto, partido y id en el response
    assert respuesta.status_code == 201
    ticket = respuesta.json()
    assert ticket["monto"] == apuesta["monto"]
    assert ticket["partido"] == apuesta["partido"]
    assert "id" in ticket  # Verifica que se haya generado un ID para la apuesta

@pytest.mark.parametrize("monto", [10, 50, 500])
def test_enviar_apuesta_devuelve_el_monto_enviado(url_base,monto):
    #arrange-url base
    url = url_base + "posts"
    apuesta = {"partido": "Real Madrid vs Barça", "monto": monto}
    #act-mandar una petición post
    respuesta = requests.post(url, json=apuesta, timeout=10)
    #assert-validar status, y monto
    assert respuesta.status_code == 201
    ticket = respuesta.json()
    assert ticket["monto"] == monto