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

# import re

# class Cliente:
#     def __init__(self, id_: int, nombre: str, email: str, telefono: str | None = None):
#         if not isinstance(id_, int) or id_ <=0:
#             raise ValueError("id debe ser entero positivo")
#         if not nombre or not nombre.strip():
#             raise ValueError("El nombre es obligatorio.")
#         if "@" not in email or "." not in email:
#             raise ValueError("Email invalido")

#         self.id = id_
#         self.nombre = nombre.strip()
#         self.email = email.strip().lower()
#         self.telefono = telefono

#     def __repr__(self) -> str:
#         return f"Cliente(id={self.id}, nombre={self.nombre!r}, email={self.email!r})" # Juliana  # 'Juliana'

#     def __str__(self) -> str:
#         return f"{self.nombre}, <{self.email}> {self.telefono}"

# c1 = Cliente(1, "Ana Gómez", "ana@example.com", "3001234567")
# c2 = Cliente(2, "Luis Pérez", "luis.perez@example.com")
# print(c1)
# print(repr(c2))

# Encapsulamiento y estados validos, primeras pruebas con pytest

# encapsulamiento: ocultar detalles internos y exponer solo lo necesario. @property, setters y getters y validaciones de lectura o solo lectura


# para que encapsular:
# convencion de privacidad... _atributo (indica que el metodo o atributo es privado)

# @property: publica un atributo encapsulado en modo solo lectura. sin un setter., podemos controlar el acceso con un setter que hace validaciones o normalizaciones.

# invariabilidad de estado: garantizar que un objeto siempre este en un estado valido. util para objetos que representan entidades del mundo real.

# que es un estado valido: un conjunto de atributos que cumplen ciertas reglas o restricciones. por ejemplo, un cliente debe tener un email valido y un nombre no vacio.

# inmutabilidad relativa: una vez creado un objeto, sus atributos no pueden cambiar. util para objetos que representan datos historicos o constantes.

#igualdad (__eq__) y hash (__hash__): definir como se comparan dos objetos y como se generan sus valores hash. importante para colecciones como conjuntos y diccionarios.

# que es un hash: un valor numerico que representa un objeto. se usa para identificar objetos en colecciones como conjuntos y diccionarios.

#Antipatrones comunes (y cómo evitarlos)

# Setters permisivos que aceptan valores sucios → añade normalización (trim, lower(), upper()) y validación (regex, longitudes).

# IDs mutables → NO: rompes igualdad/hash y colecciones.

# Meter IO/prints en los modelos → rompe separación de responsabilidades.
