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

        
