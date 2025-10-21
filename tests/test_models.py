from src.models.cliente import Cliente
from src.models.vehiculo import Vehiculo
import pytest

def test_cliente_valido():
    c = Cliente(1, "Ana", "ana@example.com", "3001112233")
    assert c.id == 1 and "Ana" in str(c)

def test_cliente_invalido():
    with pytest.raises(ValueError):
        Cliente(0, "Ana", "ana@example.com")

def test_vehiculo_valido():
    v = Vehiculo(1, 1, "abc123", "Renault", "Logan")
    assert v.placa == "ABC123"

def test_vehiculo_invalido():
    import pytest
    with pytest.raises(ValueError):
        Vehiculo(-1, 1, "XYZ987", "Chevrolet", "Onix")
