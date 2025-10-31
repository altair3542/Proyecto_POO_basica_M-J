# src/storage/csv_backend.py
from __future__ import annotations
from typing import Iterable, List, Literal
import csv
from models.cliente import Cliente
from models.vehiculo import Vehiculo

OnError = Literal["raise", "skip"]

def _require_headers(found: Iterable[str], required: Iterable[str]) -> None:
    missing = [h for h in required if h not in found]
    if missing:
        raise ValueError(f"CSV inválido, faltan columnas: {', '.join(missing)}")

def _to_int(text: str, field: str) -> int:
    try:
        return int(text)
    except Exception as ex:
        raise ValueError(f"Valor no entero en '{field}': {text!r}") from ex

def read_clientes(path: str, on_error: OnError = "raise") -> List[Cliente]:
    """
    Lee clientes desde CSV con encabezados: id,nombre,email,telefono
    Retorna lista de Cliente. on_error: 'raise' (default) o 'skip'.
    """
    out: List[Cliente] = []
    skipped = 0
    with open(path, mode="r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        _require_headers(reader.fieldnames or [], ["id", "nombre", "email", "telefono"])
        for i, row in enumerate(reader, start=2):  # fila 2 = primera de datos
            try:
                id_ = _to_int((row["id"] or "").strip(), "id")
                nombre = (row["nombre"] or "")
                email = (row["email"] or "")
                telefono = (row["telefono"] or None)
                out.append(Cliente(id_, nombre, email, telefono))
            except Exception as ex:
                if on_error == "skip":
                    skipped += 1
                    continue
                raise ValueError(f"Fila {i}: {ex}") from ex
    if skipped:
        # podrías registrar/retornar este info al caller si lo necesitas
        pass
    return out

def read_vehiculos(path: str, on_error: OnError = "raise") -> List[Vehiculo]:
    """
    Lee vehículos desde CSV con encabezados: id,cliente_id,placa,marca,modelo
    Retorna lista de Vehiculo.
    """
    out: List[Vehiculo] = []
    skipped = 0
    with open(path, mode="r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        _require_headers(reader.fieldnames or [], ["id", "cliente_id", "placa", "marca", "modelo"])
        for i, row in enumerate(reader, start=2):
            try:
                id_ = _to_int((row["id"] or "").strip(), "id")
                cliente_id = _to_int((row["cliente_id"] or "").strip(), "cliente_id")
                placa = (row["placa"] or "")
                marca = (row["marca"] or "")
                modelo = (row["modelo"] or "")
                out.append(Vehiculo(id_, cliente_id, placa, marca, modelo))
            except Exception as ex:
                if on_error == "skip":
                    skipped += 1
                    continue
                raise ValueError(f"Fila {i}: {ex}") from ex
    return out
