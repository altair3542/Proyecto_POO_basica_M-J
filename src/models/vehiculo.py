from __future__ import annotations
from dataclasses import dataclass
from .cliente import _posint, _nonempty

@dataclass(slots=True)
class Vehiculo:
    """Entidad Vehículo (sin IO)."""
    id: int
    cliente_id: int
    placa: str
    marca: str
    modelo: str

    def __init__(self, id: int, cliente_id: int, placa: str, marca: str, modelo: str):
        self.id = _posint(id, "Vehiculo.id")
        self.cliente_id = _posint(cliente_id, "Vehiculo.cliente_id")
        self.placa = _nonempty(placa, "Vehiculo.placa").upper().replace(" ", "")
        self.marca = _nonempty(marca, "Vehiculo.marca")
        self.modelo = _nonempty(modelo, "Vehiculo.modelo")

    def __str__(self) -> str:
        return f"Vehiculo[{self.id}] {self.placa} — {self.marca} {self.modelo} (cliente:{self.cliente_id})"
