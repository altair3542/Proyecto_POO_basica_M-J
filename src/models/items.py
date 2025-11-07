from __future__ import annotations
from abc import ABC, abstractmethod

class Linea(ABC):
    def __init__(self, descripcion: str):
        if not descripcion or not descripcion.strip(): raise ValueError("Descripcion obligatoria.")
        self._descripcion = descripcion.strip()

    @property
    def descripcion(self) -> str: return self._descripcion

    @abstractmethod
    def subtotal(self) -> float: ...


class Servicio(Linea):
    def __init__(self, descripcion: str, horas: float, tarifa_hora: float):
        super().__init__(descripcion)
        if horas <= 0: raise ValueError("horas menores a cero")
        if tarifa_hora < 0: raise ValueError("Tarifa hora menor a cero")
        self.horas = float(horas); self.tarifa_hora = float(tarifa_hora)
    def subtotal(self) -> float: return self.horas * self.tarifa_hora
    def __repr__(self): return f"Servicio({self.descripcion!r}, horas = {self.horas}, tarifa = {self.tarifa_hora})"


class Repuesto(Linea):
    def __init__(self, descripcion: str, cantidad: int, precio_unit: float):
        super().__init__(descripcion)
        if cantidad < 1: raise ValueError("Cantidad menor que 1")
        if precio_unit < 0: raise ValueError("precio menor a cero")
        self.cantidad = int(cantidad); self.precio_unit = float(precio_unit)
    def subtotal(self) -> float: return self.cantidad * self.precio_unit
    def __repr__(self): return f"repuesto({self.descripcion!r}, cant={self.cantidad}, unit={self.precio_unit})"
