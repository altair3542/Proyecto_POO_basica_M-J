# src/controllers/menu.py  (añade guardar/recargar si hay storage)
from typing import Callable, Optional
from views.console import title, ok, err, table, emit
from controllers.clientes import add_cliente, list_clientes
from controllers.vehiculos import add_vehiculo, list_vehiculos
from storage.repository import Storage  # el Protocol

Input = Callable[[str], str]

def _menu_text(with_storage: bool) -> str:
    base = """
[1] Listar clientes
[2] Crear cliente
[3] Listar vehículos
[4] Crear vehículo"""
    if with_storage:
        base += """
[7] Guardar datos en backend
[9] Recargar desde backend"""
    base += """
[0] Salir"""
    return base

def run(db: dict, input_func: Input = input, printer=print, storage: Optional[Storage] = None) -> None:
    emit(title("Gestor — Menú (S5)"), printer)
    with_storage = storage is not None
    MENU = _menu_text(with_storage)

    while True:
        emit(MENU.strip(), printer)
        op = input_func("Opción: ").strip()
        if op == "0":
            emit("Hasta luego.", printer); break
        try:
            handle(op, db, input_func, printer, storage)
        except Exception as ex:
            emit(err(str(ex)), printer)

def handle(op: str, db: dict, input_func: Input, printer=print, storage: Optional[Storage] = None) -> None:
    if op == "1":
        clientes = list_clientes(db)
        headers = ["id","nombre","email","tel"]
        rows = [[c.id,c.nombre,c.email,c.telefono or ""] for c in clientes]
        emit(table(headers, rows), printer)

    elif op == "2":
        c = add_cliente(db,
            int(input_func("id: ")),
            input_func("nombre: "),
            input_func("email: "),
            (lambda t: t if (t:=input_func("tel (opcional): ").strip()) else None)()
        )
        emit(ok(f"Cliente creado: {c}"), printer)

    elif op == "3":
        vehiculos = list_vehiculos(db)
        headers = ["id","cliente_id","placa","marca","modelo"]
        rows = [[v.id,v.cliente_id,v.placa,v.marca,v.modelo] for v in vehiculos]
        emit(table(headers, rows), printer)

    elif op == "4":
        v = add_vehiculo(db,
            int(input_func("id: ")),
            int(input_func("cliente_id: ")),
            input_func("placa: "),
            input_func("marca: "),
            input_func("modelo: "),
        )
        emit(ok(f"Vehículo creado: {v}"), printer)

    elif op == "7" and storage:
        storage.save_clientes(db.get("clientes", []))
        storage.save_vehiculos(db.get("vehiculos", []))
        emit(ok("Datos guardados en backend."), printer)

    elif op == "9" and storage:
        db["clientes"] = storage.load_clientes()
        db["vehiculos"] = storage.load_vehiculos()
        emit(ok("Datos recargados desde backend."), printer)

    else:
        emit(err("Opción inválida"), printer)
