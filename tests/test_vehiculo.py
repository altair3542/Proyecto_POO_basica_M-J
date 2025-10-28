# tests/test_vehiculo.py
import pytest
from models.vehiculo import Vehiculo

def test_vehiculo_placa_valida_y_normalizada():
    v = Vehiculo(1, 1, "abc123", "toyota", " corolla ")
    assert v.placa == "ABC123"
    assert v.marca == "Toyota"
    assert v.modelo == "corolla"

def test_vehiculo_placa_invalida():
    with pytest.raises(ValueError):
        Vehiculo(2, 1, "A1C-999", "toyota", "yaris")

def test_vehiculo_ids_solo_lectura():
    v = Vehiculo(3, 9, "def456", "chevrolet", "onix")
    with pytest.raises(AttributeError):
        v.id = 99
    with pytest.raises(AttributeError):
        v.cliente_id = 100
