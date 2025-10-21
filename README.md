# Gestor de Órdenes de Trabajo (CLI) — Stub MVC + JSON/CSV

Starter minimal del curso **POO Básica (MVC + JSON/CSV)**. Python 3.11+, sin frameworks ni ORMs.
Persistencia en archivos (CSV/JSON) y separación estricta de responsabilidades:

```
src/
  models/        # Entidades de dominio, reglas e invariantes (¡sin IO!)
  storage/       # Utilidades de lectura/escritura CSV y JSON
  controllers/   # Orquestación del flujo y menú CLI
  views/         # Formateo de tablas y mensajes (sin lógica de dominio)
  main.py        # Punto de entrada; selecciona backend (csv/json)
data/            # Archivos CSV/JSON
tests/           # Pruebas (pytest)
```

## Requisitos
- Python 3.11+
- (Opcional) `pytest` para ejecutar pruebas.

## Ejecutar
```bash
python -m src.main --backend csv
# o
python -m src.main --backend json
```

## Estructura de datos inicial (plantillas)
- `data/clientes.csv`: `id,nombre,email,telefono`
- `data/vehiculos.csv`: `id,cliente_id,placa,marca,modelo`
- `data/servicios.csv`: `codigo,nombre,tipo_estrategia,tarifa,otros`
- `data/ordenes.json`: arreglo de órdenes (inicialmente vacío)

## Principios (líneas rojas)
- **models/**: sin prints ni IO.
- **storage/**: solo csv/json; nunca instanciar modelos aquí.
- **controllers/**: reciben datos de `storage`, instancian modelos y llaman a `views`.
- **views/**: construyen strings (tablas/mensajes). El `print` final lo hace el controlador.

## Pruebas
```bash
pytest -q
```
