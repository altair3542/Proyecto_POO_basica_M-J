from __future__ import annotations
from typing import Iterable, List, Literal
import csv
from models.cliente import Cliente
from models.vehiculo import Vehiculo

OnError = Literal["raise", "skip"]

def _require_headers(found: Iterable[str], required:Iterable[str]) -> None:
    missing = [h for h in required if h not in found]
    if missing:
        raise ValueError(f"CSV invalido, faltan columnas: {'join(missing)'}")

def _to_int(text:str, field: str) -> int:
    try:
        return int(text)
    except Exception as ex:
        raise ValueError(f"valor no entero en '{field}':(text!r)")
from ex


