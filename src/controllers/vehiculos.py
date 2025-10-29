# src/controllers/vehiculos.py
from __future__ import annotations
from typing import Dict, List
from models.vehiculo import Vehiculo

DBType = Dict[str, list]

def add_vehiculo(db: DBType, id_: int, cliente_id: int, placa: str, marca: str, modelo: str) -> Vehiculo:
    if any(v.id == id_ for v in db.setdefault("vehiculos", [])):
        raise ValueError(f"Ya existe un vehículo con id={id_}")
    veh = Vehiculo(id_, cliente_id, placa, marca, modelo)
    db["vehiculos"].append(veh)
    return veh

def list_vehiculos(db: DBType) -> List[Vehiculo]:
    return list(db.get("vehiculos", []))
