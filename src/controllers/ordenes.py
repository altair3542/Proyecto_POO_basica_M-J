from typing import Iterable
from models.orden import Orden
from models.items import Servicio, Repuesto

DB = dict  # alias

def create_orden(db: DB, id_: int, cliente_id: int, vehiculo_id: int, iva_pct: float = 0.19, descuento_pct: float = 0.0) -> Orden:
    db.setdefault("ordenes", [])
    if any(o.id == id_ for o in db["ordenes"]):
        raise ValueError(f"Orden id={id_} ya existe")
    o = Orden(id_, cliente_id, vehiculo_id, iva_pct, descuento_pct)
    db["ordenes"].append(o)
    return o

def list_ordenes(db: DB) -> list[Orden]:
    return list(db.get("ordenes", []))

def add_servicio(db: DB, orden_id: int, descripcion: str, horas: float, tarifa_hora: float) -> None:
    o = _get_orden(db, orden_id); o.agregar_linea(Servicio(descripcion, horas, tarifa_hora))

def add_repuesto(db: DB, orden_id: int, descripcion: str, cantidad: int, precio_unit: float) -> None:
    o = _get_orden(db, orden_id); o.agregar_linea(Repuesto(descripcion, cantidad, precio_unit))

def cambiar_estado(db: DB, orden_id: int, nuevo_estado: str) -> None:
    _get_orden(db, orden_id).cambiar_estado(nuevo_estado)

def detalle_orden(db: DB, orden_id: int) -> Orden:
    return _get_orden(db, orden_id)

def _get_orden(db: DB, orden_id: int) -> Orden:
    for o in db.get("ordenes", []):
        if o.id == orden_id: return o
    raise ValueError(f"Orden id={orden_id} no encontrada")
