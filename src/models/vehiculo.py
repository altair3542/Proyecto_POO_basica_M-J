class Vehiculo:
    """
    Entidad Vehículo (S1).
    - Validación mínima: ids positivos, placa no vacía.
    - Normaliza placa a MAYÚSCULAS y marca a Title Case.
    """
    def __init__(self, id_: int, cliente_id: int, placa: str, marca: str, modelo: str):
        if id_ <= 0 or cliente_id <= 0:
            raise ValueError("id_ y cliente_id deben ser enteros positivos")
        if not placa or not placa.strip():
            raise ValueError("placa es obligatoria")

        self.id = id_
        self.cliente_id = cliente_id
        self.placa = placa.strip().upper()
        self.marca = marca.strip().title()
        self.modelo = modelo.strip()

    def __repr__(self) -> str:
        return (f"Vehiculo(id={self.id}, cliente_id={self.cliente_id}, "
                f"placa={self.placa!r}, marca={self.marca!r}, modelo={self.modelo!r})")

    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} [{self.placa}]"
