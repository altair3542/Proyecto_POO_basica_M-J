import os
from controllers.menu import run
from storage.repository import make_storage

def main():
    backend = os.getenv("BACKEND", "csv")  # "mem" | "csv" | "json"
    data_dir = os.getenv("DATA_DIR", "data")
    storage = make_storage(backend, data_dir)

    # Poblar el "db" del ciclo de vida de la app
    db = {
        "clientes": storage.load_clientes(),
        "vehiculos": storage.load_vehiculos(),
    }

    # Pasamos storage opcional al menú para permitir Guardar/Recargar
    run(db, storage=storage)

if __name__ == "__main__":
    main()
