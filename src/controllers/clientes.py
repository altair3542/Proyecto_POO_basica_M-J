# src/controllers/clientes.py
from __future__ import annotations
from typing import Dict, List
from models.cliente import Cliente

# "Base de datos" en memoria: dict con listas
DBType = Dict[str, list]

def add_cliente(db: DBType, id_: int, nombre: str, email: str, telefono: str | None = None) -> Cliente:
    # Validación de unicidad por id (dominio decide; en S2: igualdad por id)
    if any(c.id == id_ for c in db.setdefault("clientes", [])):
        raise ValueError(f"Ya existe un cliente con id={id_}")
    cli = Cliente(id_, nombre, email, telefono)
    db["clientes"].append(cli)
    return cli

def list_clientes(db: DBType) -> List[Cliente]:
    return list(db.get("clientes", []))
