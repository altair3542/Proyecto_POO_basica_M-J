# src/models/cliente.py
from __future__ import annotations
import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")  # simple y suficiente para S2

class Cliente:
    """
    Entidad Cliente (S2): estado válido, encapsulado.
    - id: entero positivo, solo lectura.
    - nombre: string no vacío, saneado.
    - email: validado con regex mínima, normalizado a lower().
    - telefono (opcional): dígitos 7..15 (se guarda normalizado, solo dígitos).
    - Igualdad y hash por id (identidad de dominio).
    """
    __slots__ = ("_id", "_nombre", "_email", "_telefono")

    def __init__(self, id_: int, nombre: str, email: str, telefono: str | None = None):
        # id (solo lectura)
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError("id debe ser entero positivo")
        self._id = id_

        # nombre
        self.nombre = nombre  # pasa por setter

        # email
        self.email = email    # pasa por setter

        # telefono (opcional)
        self.telefono = telefono  # pasa por setter (permite None)

    # --- id: solo lectura ---
    @property
    def id(self) -> int:
        return self._id

    # --- nombre ---
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if value is None:
            raise ValueError("nombre es obligatorio")
        v = value.strip()
        if len(v) < 2:
            raise ValueError("nombre muy corto")
        self._nombre = v

    # --- email ---
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        if value is None:
            raise ValueError("email es obligatorio")
        v = value.strip().lower()
        if not _EMAIL_RE.match(v):
            raise ValueError("email inválido")
        self._email = v

    # --- telefono (opcional) ---
    @property
    def telefono(self) -> str | None:
        return self._telefono

    @telefono.setter
    def telefono(self, value: str | None) -> None:
        if value is None:
            self._telefono = None
            return
        digits = "".join(ch for ch in str(value) if ch.isdigit())
        if not (7 <= len(digits) <= 15):
            raise ValueError("telefono inválido (7..15 dígitos)")
        self._telefono = digits

    # --- representaciones ---
    def __repr__(self) -> str:
        return f"Cliente(id={self.id}, nombre={self.nombre!r}, email={self.email!r})"

    def __str__(self) -> str:
        return f"{self.nombre} <{self.email}>"

    # --- igualdad / hashing por id ---
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cliente):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(("Cliente", self.id))
