from __future__ import annotations
from pathlib import Path
import json
from typing import Any, List, Dict

def read_ordenes(data_dir: Path) -> List[Dict[str, Any]]:
    path = data_dir / "ordenes.json"
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def write_ordenes(data_dir: Path, ordenes: List[Dict[str, Any]]) -> None:
    path = data_dir / "ordenes.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(ordenes, f, ensure_ascii=False, indent=2)
