from __future__ import annotations
from pathlib import Path
import csv
from typing import Iterable, Dict, List

def _read_csv(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]

def read_clientes(data_dir: Path) -> List[Dict[str, str]]:
    """Lee clientes desde CSV (dicts)."""
    return _read_csv(data_dir / "clientes.csv")

def read_vehiculos(data_dir: Path) -> List[Dict[str, str]]:
    """Lee vehículos desde CSV (dicts)."""
    return _read_csv(data_dir / "vehiculos.csv")

def read_servicios(data_dir: Path) -> List[Dict[str, str]]:
    """Lee servicios desde CSV (dicts)."""
    return _read_csv(data_dir / "servicios.csv")
