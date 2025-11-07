from __future__ import annotations
from typing import List
from .items import Linea

class Orden:
    ESTADOS = {"ABIERTA", "EN_PROCESO", "CERRADA", "ANULADA"}
    def __init__(self, id_: int, cliente_id: int, vehiculo_id: int, iva_pct: float = 0.19, descuento_pct: float = 0.0):
        if id_ <= 0 or cliente_id <= 0 or vehiculo_id <= 0: raise ValueError("los id's deben ser posivos")
        self._id = id_; self._cliente_id = cliente_id; self._vehiculo_id = vehiculo_id
        self._estado = "ABIERTA"
        self.iva_pct = float(iva_pct); self.descuento_pct = float(descuento_pct)
        self._lineas = List[Linea] = []

    @property
    def id(self) -> int: return self._id

    @property
    def cliente_id(self) -> int: return self._cliente_id

    @property
    def vehiculo_id(self) -> int: return self._vehiculo_id

    @property
    def estado(self) -> str: return self._estado


    def _editable(self) -> bool: return self._estado in {"ABIERTA", "EN_PROCESO"}

    def cambiar_estado(self, nuevo: str) -> None:
        n = nuevo.strip().upper().replace(" ", "_")
        if n not in self.ESTADOS: raise ValueError("Estado invalido")
        trans_ok = (
            (self._estado, n) in {("ABIERTA", "EN_PROCESO"), ("EN_PROCESO", "CERRADA"), ("ABIERTA", "ANULADA")}
            or self._estado == n
        )
        if not trans_ok: raise ValueError(f"La transicion no esta perimitida {self._estado}")
        self._estado = n

    def agregar_linea(self, linea: Linea) ->None:
        if not self._editable(): raise RuntimeError("no editable en estado actual")
        self._lineas.append(linea)

    def subtotal(self) -> float:
        return sum(l.subtotal() for l in self._lineas)

    def total(self) -> float:
        sub = self.subtotal()
        base = max(0.0, sub - sub * self.descuento_pct)
        return round(base + base * self.iva_pct, 2)

    def lineas(self) -> list[Linea]:
        return list(self._lineas)

    def __repr__(self):
        return f"Orden(id={self.id}, estado={self.estado}, lineas={len(self._lineas)}, total={self.total()})"
