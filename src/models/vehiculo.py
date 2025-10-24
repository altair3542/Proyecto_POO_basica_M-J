# src/models/vehiculo.py
from __future__ import annotations
import re

# Patrón típico Colombia (carro): ABC123. (Motocicleta varía; lo ajustaremos si lo necesitas)
_PLACA_RE = re.compile(r"^[A-Z]{3}\d{3}$")

class Vehiculo:
    """
    Entidad Vehículo (S2): estado válido, encapsulado.
    - id y cliente_id: enteros positivos, solo lectura.
    - placa: formato ABC123 (normalizada a upper), validada.
    - marca/modelo: no vacíos, saneados; marca en Title Case.
    - Igualdad y hash por id (identidad de dominio).
    """
    __slots__ = ("_id", "_cliente_id", "_placa", "_marca", "_modelo")

    def __init__(self, id_: int, cliente_id: int, placa: str, marca: str, modelo: str):
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError("id debe ser entero positivo")
        if not isinstance(cliente_id, int) or cliente_id <= 0:
            raise ValueError("cliente_id debe ser entero positivo")
        self._id = id_
        self._cliente_id = cliente_id

        self.placa = placa    # setter valida y normaliza
        self.marca = marca
        self.modelo = modelo

    # --- solo lectura ---
    @property
    def id(self) -> int:
        return self._id

    @property
    def cliente_id(self) -> int:
        return self._cliente_id

    # --- placa ---
    @property
    def placa(self) -> str:
        return self._placa

    @placa.setter
    def placa(self, value: str) -> None:
        if value is None:
            raise ValueError("placa es obligatoria")
        v = value.strip().upper()
        if not _PLACA_RE.match(v):
            raise ValueError("placa inválida (esperado ABC123)")
        self._placa = v

    # --- marca ---
    @property
    def marca(self) -> str:
        return self._marca

    @marca.setter
    def marca(self, value: str) -> None:
        if value is None:
            raise ValueError("marca es obligatoria")
        v = value.strip()
        if not v:
            raise ValueError("marca es obligatoria")
        self._marca = v.title()

    # --- modelo ---
    @property
    def modelo(self) -> str:
        return self._modelo

    @modelo.setter
    def modelo(self, value: str) -> None:
        if value is None:
            raise ValueError("modelo es obligatorio")
        v = value.strip()
        if not v:
            raise ValueError("modelo es obligatorio")
        self._modelo = v

    # --- representaciones ---
    def __repr__(self) -> str:
        return (f"Vehiculo(id={self.id}, cliente_id={self.cliente_id}, "
                f"placa={self.placa!r}, marca={self.marca!r}, modelo={self.modelo!r})")

    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} [{self.placa}]"

    # --- igualdad / hashing por id ---
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vehiculo):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(("Vehiculo", self.id))
