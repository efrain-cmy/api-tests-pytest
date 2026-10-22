def descontar_apuesta(saldo, monto):
    if monto > saldo:
        raise ValueError("No hay suficiente saldo para realizar la apuesta.")

    return saldo - monto