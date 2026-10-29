import pytest
from tests.factories import crear_apuesta

@pytest.mark.smoke
def test_apuestas_devuelve_201_y_ticket_con_id(url_apuestas,api):
    apuesta = crear_apuesta()
    #act-mandar una petición post
    respuesta  = api.post(url_apuestas, json=apuesta, timeout=10)
    #assert-validar status,monto, partido y id en el response
    assert respuesta.status_code == 201
    ticket = respuesta.json()
    assert ticket["monto"] == apuesta["monto"]
    assert ticket["partido"] == apuesta["partido"]
    assert "id" in ticket  # Verifica que se haya generado un ID para la apuesta

@pytest.mark.parametrize("monto", [10, 50, 500])
@pytest.mark.regression
def test_enviar_apuesta_devuelve_el_monto_enviado(url_apuestas,monto, api):
    apuesta = crear_apuesta(monto=monto)
    #act-mandar una petición post
    respuesta = api.post(url_apuestas, json=apuesta, timeout=10)
    #assert-validar status, y monto
    assert respuesta.status_code == 201
    ticket = respuesta.json()
    assert ticket["monto"] == monto

@pytest.mark.smoke
def test_ticket_existente_devuelve_200_y_el_id(url_apuestas, api):
    #act-mandar una petición get
    respuesta = api.get(url_apuestas + "1", timeout=10)
    #assert-validar status, y id
    assert respuesta.status_code == 200
    ticket = respuesta.json()
    assert ticket["id"] == 1

@pytest.mark.regression
def test_ticket_inexistente_devuelve_404(url_apuestas, api):
    #act-mandar una petición get
    respuesta = api.get(url_apuestas + "99099", timeout=10)
    #assert-validar status
    assert respuesta.status_code == 404
