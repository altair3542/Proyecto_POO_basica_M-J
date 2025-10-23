from models.cliente import Cliente
from models.vehiculo import Vehiculo

def main():
    # 3 clientes
    c1 = Cliente(1, "Ana Gómez", "ana@example.com", "3001234567")
    c2 = Cliente(2, "Luis Pérez", "luis.perez@example.com")
    c3 = Cliente(3, "Mery Cano", "mery@ejemplo.com")

    # 2 vehículos
    v1 = Vehiculo(1, c1.id, "abc123", "toyota", "corolla")
    v2 = Vehiculo(2, c2.id, "def456", "chevrolet", "onix")

    # Hoy no hay views ni controllers: imprimimos directo desde main
    print("=== CLIENTES ===")
    print(c1)  # usa __str__
    print(c2)
    print(c3)

    print("\n=== VEHÍCULOS ===")
    print(v1)  # usa __str__
    print(v2)

if __name__ == "__main__":
    main()
