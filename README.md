# api-tests-pytest

## ¿Qué prueba este repo?

Pruebas de API con pytest sobre el recurso `/posts` de
[JSONPlaceholder](https://jsonplaceholder.typicode.com), usado como simulación de un endpoint de apuestas.
Cubre los verbos POST, GET, PUT y DELETE: status code, estructura del JSON (jsonschema) y los datos devueltos.
También incluye una prueba unitaria de la función `descontar_apuesta` en `src/`.

## ¿Cómo lo corro?

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Correr todo:

```bash
pytest
```

Correr solo smoke:

```bash
pytest -m smoke
```

Generar el reporte HTML:

```bash
pytest --html=reporte.html --self-contained-html
```

## ¿Cómo está organizado?

- `tests/conftest.py` — fixtures: URL base, URL de apuestas y sesión HTTP compartida.
- `tests/factories.py` — `crear_apuesta()`, arma el payload de una apuesta con monto configurable.
- `tests/schemas.py` — esquemas JSON para validar la respuesta de los tickets.
- `tests/test_apuestas.py` — pruebas de API: crear, leer, modificar y eliminar apuestas (casos felices y 404).
- `tests/test_saldo.py` — pruebas unitarias de `descontar_apuesta`: saldo resultante y rechazo por saldo insuficiente.

