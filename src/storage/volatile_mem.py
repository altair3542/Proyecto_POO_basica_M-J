
from __future__ import annotations
from typing import List
from models.cliente import Cliente
from models.vehiculo import Vehiculo

class MemStorage:
    def __init__(self):
        self._clientes: List[Cliente] = []
        self._vehiculos: List[Vehiculo] = []

    def load_clientes(self) -> List[Cliente]:
        return list(self._clientes)

    def load_vehiculos(self) -> List[Vehiculo]:
        return list(self._vehiculos)

    def save_clientes(self, clientes: List[Cliente]) -> None:
        self._clientes = list(clientes)

    def save_vehiculos(self, vehiculos: List[Vehiculo]) -> None:
        self._vehiculos = list(vehiculos)
