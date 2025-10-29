# src/controllers/menu.py
from __future__ import annotations
from typing import Callable, Dict
from views.console import format_title, format_error, format_success, format_table, emit
from controllers.clientes import add_cliente, list_clientes
from controllers.vehiculos import add_vehiculo, list_vehiculos

InputFn = Callable[[str], str]
DBType = Dict[str, list]

MENU = """
[1] Listar clientes
[2] Crear cliente
[3] Listar vehículos
[4] Crear vehículo
[0] Salir
"""

def run(db: DBType, input_func: InputFn = input, printer=print) -> None:
    emit(format_title("Gestor de Órdenes — Menú (S3)"), printer)
    while True:
        emit(MENU.strip(), printer)
        opcion = input_func("Opción: ").strip()
        if opcion == "0":
            emit("Hasta luego.", printer)
            break
        try:
            handle_option(opcion, db, input_func, printer)
        except Exception as ex:
            emit(format_error(str(ex)), printer)

def handle_option(opcion: str, db: DBType, input_func: InputFn, printer=print) -> None:
    if opcion == "1":
        clientes = list_clientes(db)
        headers = ["id", "nombre", "email", "telefono"]
        rows = [(c.id, c.nombre, c.email, c.telefono or "") for c in clientes]
        emit(format_table(headers, rows), printer)

    elif opcion == "2":
        id_ = int(input_func("id: "))
        nombre = input_func("nombre: ")
        email = input_func("email: ")
        telefono = input_func("telefono (opcional): ").strip() or None
        cli = add_cliente(db, id_, nombre, email, telefono)
        emit(format_success(f"Cliente creado: {cli}"), printer)

    elif opcion == "3":
        vehiculos = list_vehiculos(db)
        headers = ["id", "cliente_id", "placa", "marca", "modelo"]
        rows = [(v.id, v.cliente_id, v.placa, v.marca, v.modelo) for v in vehiculos]
        emit(format_table(headers, rows), printer)

    elif opcion == "4":
        id_ = int(input_func("id: "))
        cliente_id = int(input_func("cliente_id: "))
        placa = input_func("placa: ")
        marca = input_func("marca: ")
        modelo = input_func("modelo: ")
        veh = add_vehiculo(db, id_, cliente_id, placa, marca, modelo)
        emit(format_success(f"Vehículo creado: {veh}"), printer)

    else:
        emit(format_error("Opción inválida"), printer)
