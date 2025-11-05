from __future__ import annotations
from typing import List, Any
import os, json, tempfile
from models.cliente import Cliente
from models.vehiculo import Vehiculo

def _atomic_dump(path: str, data: Any) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path) or ".", prefix=".tmp_", suffix=".json")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    os.replace(tmp, path)

class JsonStorage:
    def __init__(self, base_dir: str = "data"):
        self.base = base_dir
        os.makedirs(self.base, exist_ok=True)

    # Convierte objetos a dicts simples (sin tocar los modelos)
    @staticmethod
    def _cliente_to_dict(c: Cliente) -> dict:
        return {"id": c.id, "nombre": c.nombre, "email": c.email, "telefono": c.telefono}

    @staticmethod
    def _vehiculo_to_dict(v: Vehiculo) -> dict:
        return {"id": v.id, "cliente_id": v.cliente_id, "placa": v.placa, "marca": v.marca, "modelo": v.modelo}

    # ---------- Lectura ----------
    def load_clientes(self) -> List[Cliente]:
        path = os.path.join(self.base, "clientes.json")
        if not os.path.exists(path): return []
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        out: List[Cliente] = []
        for i, row in enumerate(data, start=1):
            out.append(Cliente(int(row["id"]), row["nombre"], row["email"], row.get("telefono")))
        return out

    def load_vehiculos(self) -> List[Vehiculo]:
        path = os.path.join(self.base, "vehiculos.json")
        if not os.path.exists(path): return []
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        out: List[Vehiculo] = []
        for i, row in enumerate(data, start=1):
            out.append(Vehiculo(int(row["id"]), int(row["cliente_id"]), row["placa"], row["marca"], row["modelo"]))
        return out

    # ---------- Escritura ----------
    def save_clientes(self, clientes: List[Cliente]) -> None:
        path = os.path.join(self.base, "clientes.json")
        payload = [self._cliente_to_dict(c) for c in clientes]
        _atomic_dump(path, payload)

    def save_vehiculos(self, vehiculos: List[Vehiculo]) -> None:
        path = os.path.join(self.base, "vehiculos.json")
        payload = [self._vehiculo_to_dict(v) for v in vehiculos]
        _atomic_dump(path, payload)
