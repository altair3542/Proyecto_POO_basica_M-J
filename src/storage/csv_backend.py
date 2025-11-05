# src/storage/csv_backend.py
from __future__ import annotations
from typing import Iterable, List, Literal
import os, csv, tempfile
from models.cliente import Cliente
from models.vehiculo import Vehiculo

OnError = Literal["raise", "skip"]

def _require_headers(found: Iterable[str], required: Iterable[str]) -> None:
    missing = [h for h in required if h not in found]
    if missing:
        raise ValueError(f"CSV inválido, faltan columnas: {', '.join(missing)}")

def _to_int(text: str, field: str) -> int:
    try:
        return int(text)
    except Exception as ex:
        raise ValueError(f"Valor no entero en '{field}': {text!r}") from ex

def _atomic_write(path: str, text: str) -> None:
    #escribir en un tmp y vamos a renombrar el archivo generado
    d = os.path.dirname(path) or "."
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".tmp_",suffix=".csv")
    with os.fdopen(fd, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    os.replace(tmp, path)

class CsvStorage:
    def __init__(self, base_dir: str = "data"):
        self.base = base_dir
        os.makedirs(self.base, exist_ok=True)

    # ---------- Lectura ----------
    def load_clientes(self) -> List[Cliente]:
        path = os.path.join(self.base, "clientes.csv")
        out: List[Cliente] = []
        with open(path, "r", encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh)
            _require_headers(reader.fieldnames, ["id","nombre","email","telefono"])
            for i, row in enumerate(reader, start=2):
                id_ = _to_int((row["id"] or "").strip(), "id")
                out.append(Cliente(id_, row["nombre"] or "", row["email"] or "", row.get("telefono") or None))
        return out

    def load_vehiculos(self) -> List[Vehiculo]:
        path = os.path.join(self.base, "vehiculos.csv")
        out: List[Vehiculo] = []
        with open(path, "r", encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh)
            _require_headers(reader.fieldnames, ["id","cliente_id","placa","marca","modelo"])
            for i, row in enumerate(reader, start=2):
                id_ = _to_int((row["id"] or "").strip(), "id")
                cliente_id = _to_int((row["cliente_id"] or "").strip(), "cliente_id")
                out.append(Vehiculo(id_, cliente_id, row["placa"] or "", row["marca"] or "", row["modelo"] or ""))
        return out

    # ---------- Escritura ----------
    def save_clientes(self, clientes: List[Cliente]) -> None:
        headers = ["id","nombre","email","telefono"]
        # Construimos el CSV en memoria para escritura atómica
        from io import StringIO
        buf = StringIO()
        w = csv.DictWriter(buf, fieldnames=headers, lineterminator="\n")
        w.writeheader()
        for c in clientes:
            w.writerow({"id": c.id, "nombre": c.nombre, "email": c.email, "telefono": c.telefono or ""})
        _atomic_write(os.path.join(self.base, "clientes.csv"), buf.getvalue())

    def save_vehiculos(self, vehiculos: List[Vehiculo]) -> None:
        headers = ["id","cliente_id","placa","marca","modelo"]
        from io import StringIO
        buf = StringIO()
        w = csv.DictWriter(buf, fieldnames=headers, lineterminator="\n")
        w.writeheader()
        for v in vehiculos:
            w.writerow({"id": v.id, "cliente_id": v.cliente_id, "placa": v.placa,
                        "marca": v.marca, "modelo": v.modelo})
        _atomic_write(os.path.join(self.base, "vehiculos.csv"), buf.getvalue())
