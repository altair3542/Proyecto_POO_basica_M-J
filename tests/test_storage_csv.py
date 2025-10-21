from pathlib import Path
from src.storage.csv_backend import read_clientes, read_vehiculos

def test_read_clientes(tmp_path: Path):
    p = tmp_path / "clientes.csv"
    p.write_text("id,nombre,email,telefono\n1,Ana,ana@example.com,\n", encoding="utf-8")
    rows = read_clientes(tmp_path)
    assert rows and rows[0]["nombre"] == "Ana"

def test_read_vehiculos(tmp_path: Path):
    p = tmp_path / "vehiculos.csv"
    p.write_text("id,cliente_id,placa,marca,modelo\n1,1,ABC123,Renault,Logan\n", encoding="utf-8")
    rows = read_vehiculos(tmp_path)
    assert rows and rows[0]["placa"] == "ABC123"
