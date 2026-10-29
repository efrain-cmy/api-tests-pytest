# tests/test_saldo.py
import pytest
from src.first_funtion import descontar_apuesta



@pytest.mark.parametrize(
    "saldo, monto, esperado",
    [
        (100, 30, 70),
        (50, 20, 30),
        (80, 80, 0),
    ]
)
@pytest.mark.regression
def test_descontar_apuesta_deja_saldo_esperado(saldo, monto, esperado):
    # Act: hacer la acción que quiero probar
    nuevo_saldo = descontar_apuesta(saldo, monto)
    #assert: verificar que el resultado es el esperado
    assert nuevo_saldo == esperado

@pytest.mark.regression
def test_descontar_apuesta_rechaza_saldo_insuficiente():
    saldo = 50
    monto = 60

    with pytest.raises(ValueError) as exc_info:
        descontar_apuesta(saldo, monto)
    #assert: verificar que el mensaje de error es el esperado
    assert str(exc_info.value) == "No hay suficiente saldo para realizar la apuesta."


