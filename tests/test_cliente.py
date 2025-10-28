# tests/test_cliente.py
import pytest
from models.cliente import Cliente

def test_cliente_email_normalizado_y_valido():
    c = Cliente(1, " Ana ", "ANA@EXAMPLE.com", "300-123-4567")
    assert c.nombre == "Ana"
    assert c.email == "ana@example.com"
    assert c.telefono == "3001234567"

def test_cliente_email_invalido():
    with pytest.raises(ValueError):
        Cliente(2, "Luis", "sin-arroba", None)

def test_cliente_id_solo_lectura():
    c = Cliente(3, "Mery", "mery@ex.com")
    with pytest.raises(AttributeError):
        c.id = 99

def test_cliente_igualdad_y_hash_por_id():
    a = Cliente(10, "A", "a@ex.com")
    b = Cliente(10, "B", "b@ex.com")  # mismo id, distinto estado
    c = Cliente(11, "A", "a@ex.com")  # id distinto, mismo email
    assert a == b
    assert a != c
    s = {a, b, c}
    # a y b colapsan en el mismo bucket por id
    assert len(s) == 2
