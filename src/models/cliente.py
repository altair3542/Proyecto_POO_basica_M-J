from __future__ import annotations
from dataclasses import dataclass

def _nonempty(s: str, field: str) -> str:
    if not isinstance(s, str) or not s.strip():
        raise ValueError(f"{field} no puede estar vacío")
    return s.strip()

def _posint(n: int, field: str) -> int:
    if not isinstance(n, int) or n <= 0:
        raise ValueError(f"{field} debe ser un entero positivo")
    return n

@dataclass(slots=True)
class Cliente:
    """Entidad Cliente (sin IO). SRP: representar un cliente válido."""
    id: int
    nombre: str
    email: str
    telefono: str = ""

    def __init__(self, id: int, nombre: str, email: str, telefono: str = ""):
        self.id = _posint(id, "Cliente.id")
        self.nombre = _nonempty(nombre, "Cliente.nombre")
        self.email = _nonempty(email, "Cliente.email")
        self.telefono = (telefono or "").strip()

    def __str__(self) -> str:
        return f"Cliente[{self.id}] {self.nombre} <{self.email}>"
