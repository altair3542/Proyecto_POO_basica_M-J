from __future__ import annotations
from typing import List, Protocol
from models.cliente import Cliente
from models.vehiculo import Vehiculo

class Storage(Protocol):
    # Carga completa (solo lectura de origen)
    def load_clientes(self) -> List[Cliente]: ...
    def load_vehiculos(self) -> List[Vehiculo]: ...

    # escritura completa (reemplazando el archivo totalmente.)
    def save_clientes(self, clientes: list[Cliente]) -> None: ...
    def save_vehiculos(self, vehiculos: list[Vehiculo]) -> None: ...

def make_storage(kind: str, base_dir: str) -> Storage:
    kind = (kind or "mem").lower()
    if kind == "csv":
        from .csv_backend import CsvStorage
        return CsvStorage(base_dir)
    if kind == "json":
        from .json_backend import JsonStorage
        return JsonStorage(base_dir)
    from .volatile_mem import MemStorage
    return MemStorage()

