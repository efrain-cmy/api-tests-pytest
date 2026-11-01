import pytest
from tests.factories import crear_apuesta
from jsonschema import validate
from tests.schemas import TICKET_SCHEMA, TICKET_GUARDADO_SCHEMA

@pytest.mark.smoke
def test_apuestas_devuelve_201_y_ticket_con_id(url_apuestas,api):
    apuesta = crear_apuesta()
    #act-mandar una petición post
    respuesta  = api.post(url_apuestas, json=apuesta, timeout=10)
    #assert-validar status,monto, partido y id en el response
    assert respuesta.status_code == 201
    ticket = respuesta.json()
    validate(ticket, TICKET_SCHEMA)
    assert ticket["monto"] == apuesta["monto"]
    assert ticket["partido"] == apuesta["partido"]


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

@pytest.mark.parametrize("ticket_Id", [1, 2, 3, 50, 100])
@pytest.mark.smoke
def test_ticket_existente_devuelve_200_y_el_id(url_apuestas, api, ticket_Id):
    #act-mandar una petición get
    respuesta = api.get(url_apuestas + f"{ticket_Id}", timeout=10)
    #assert-validar status, y id
    assert respuesta.status_code == 200
    ticket = respuesta.json()
    validate(ticket, TICKET_GUARDADO_SCHEMA )
    assert ticket["id"] == ticket_Id

@pytest.mark.parametrize("ticket_Id", [0, 9999])
@pytest.mark.regression
def test_ticket_inexistente_devuelve_404(url_apuestas, api, ticket_Id):
    #act-mandar una petición get
    respuesta = api.get(url_apuestas + f"{ticket_Id}", timeout=10)
    #assert-validar status
    assert respuesta.status_code == 404
