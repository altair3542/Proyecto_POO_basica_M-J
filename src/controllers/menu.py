from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict
from ..storage import csv_backend, json_backend
from ..models.cliente import Cliente
from ..models.vehiculo import Vehiculo
from ..views.tables import format_table, message_info

@dataclass
class AppConfig:
    data_dir: Path
    backend: str = "csv"  # "csv" o "json" (para órdenes)

class MenuCLI:
    def __init__(self, cfg: AppConfig) -> None:
        self.cfg = cfg

    def run(self) -> None:
        while True:
            print("\n=== Gestor de Órdenes (Stub) ===")
            print("1) Listar clientes (CSV)")
            print("2) Listar vehículos (CSV)")
            print("0) Salir")
            op = input("> ").strip()
            if op == "1":
                self.listar_clientes()
            elif op == "2":
                self.listar_vehiculos()
            elif op == "0":
                print("Hasta luego.")
                break
            else:
                print("Opción inválida.")

    def listar_clientes(self) -> None:
        raw = csv_backend.read_clientes(self.cfg.data_dir)
        clientes = []
        for r in raw:
            try:
                clientes.append(Cliente(int(r["id"]), r["nombre"], r["email"], r.get("telefono","")))
            except Exception as e:
                print(message_info(f"Fila inválida en clientes.csv: {e}"))
        rows = [ {"id": c.id, "nombre": c.nombre, "email": c.email, "telefono": c.telefono} for c in clientes ]
        if not rows:
            print(message_info("No hay clientes."))
            return
        print(format_table(rows, ["id","nombre","email","telefono"], ["ID","Nombre","Email","Teléfono"]))

    def listar_vehiculos(self) -> None:
        raw = csv_backend.read_vehiculos(self.cfg.data_dir)
        vehiculos = []
        for r in raw:
            try:
                vehiculos.append(Vehiculo(int(r["id"]), int(r["cliente_id"]), r["placa"], r["marca"], r["modelo"]))
            except Exception as e:
                print(message_info(f"Fila inválida en vehiculos.csv: {e}"))
        rows = [ {"id": v.id, "cliente_id": v.cliente_id, "placa": v.placa, "marca": v.marca, "modelo": v.modelo} for v in vehiculos ]
        if not rows:
            print(message_info("No hay vehículos."))
            return
        print(format_table(rows, ["id","cliente_id","placa","marca","modelo"], ["ID","Cliente","Placa","Marca","Modelo"]))
