# Que es POO:

# la POO es un paradigma de programacion que nos permite convertir entidades del mundo real en objetos dentro de nuestro codigo.

# Una clase es un molde o plantilla que define las propiedades y comportamientos comunes de un conjunto de objetos.

#instancia: es un objeto creado a partir de una clase.

# atributos: son las caracteristicas o propiedades que definen el estado de un objeto.

# comportamientos: son las acciones o metodos que un objeto puede realizar.

# class Persona:
#     def __init__(self, ojos, boca, cuerpo, estatura, peso, genero):
#         self.ojos = ojos,
#         self.boca = boca

# estos atributos pueden ser de instancia o de clase...
# attributos unicos o que viven en cada instancia.

#atributos de clase: como su nombre lo dice, viven en la clase...

# PILARES: son las bases especificas de la programacion orientada a objetos.

# herencia: reutilizar comportamientos o atributos de una clase padre a una clase hija.

# Polimorfismo: dos clases pueden compartir el mismo metodo o comportamiento, pero este puede actuar diferente.

# encapsulamiento: oculta detalles internos y expone solo lo necesario.

# Abstraccion...

import re

class Cliente:
    def __init__(self, id_: int, nombre: str, email: str, telefono: str | None = None):
        if not isinstance(id_, int) or id_ <=0:
            raise ValueError("id debe ser entero positivo")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")
        if "@" not in email or "." not in email:
            raise ValueError("Email invalido")

        self.id = id_
        self.nombre = nombre.strip()
        self.email = email.strip().lower()
        self.telefono = telefono

    def __repr__(self) -> str:
        return f"Cliente(id={self.id}, nombre={self.nombre!r}, email={self.email!r})" # Juliana  # 'Juliana'

    def __str__(self) -> str:
        return f"{self.nombre}, <{self.email}> {self.telefono}"

c1 = Cliente(1, "Ana Gómez", "ana@example.com", "3001234567")
c2 = Cliente(2, "Luis Pérez", "luis.perez@example.com")
print(c1)
print(repr(c2))
