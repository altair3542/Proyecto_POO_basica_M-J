class Cliente:
    """
    Entidad Cliente (S1).
    - Validación mínima: id positivo, nombre no vacío, email con '@' y '.'
    - Sin prints ni IO: solo reglas del dominio.
    """
    def __init__(self, id_: int, nombre: str, email: str, telefono: str | None = None):
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError("id_ debe ser entero positivo")
        if not nombre or not nombre.strip():
            raise ValueError("nombre es obligatorio")
        if "@" not in email or "." not in email:
            raise ValueError("email inválido (S1)")

        self.id = id_
        self.nombre = nombre.strip()
        self.email = email.strip().lower()
        self.telefono = telefono

    def __repr__(self) -> str:
        # !r = usa repr() → útil para depurar (muestra comillas, None, espacios)
        return f"Cliente(id={self.id}, nombre={self.nombre!r}, email={self.email!r})"

    def __str__(self) -> str:
        # Amigable para usuarios
        return f"{self.nombre} <{self.email}>"
