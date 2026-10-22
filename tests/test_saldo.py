# tests/test_saldo.py

import pytest


def descontar_apuesta(saldo, monto):
    if monto > saldo:
        raise ValueError("No hay suficiente saldo para realizar la apuesta.")

    return saldo - monto


def test_apostar_30_con_saldo_100_deja_70():
    # Arrange: preparar los datos
    saldo = 100
    monto = 30

    # Act: hacer la acción que quiero probar
    nuevo_saldo = descontar_apuesta(saldo, monto)

    # Assert: verificar
    assert nuevo_saldo == 70

def test_apostar_mas_de_saldo_lanza_error():
    # Arrange
    saldo = 50
    monto = 60

    # Act & Assert
    with pytest.raises(ValueError):
       assert descontar_apuesta(saldo, monto)

def test_apostar_igual_a_saldo_deja_cero():
    # Arrange
    saldo = 80
    monto = 80

    # Act
    nuevo_saldo = descontar_apuesta(saldo, monto)
    # Assert    
    assert nuevo_saldo == 0
