import os
from controllers.menu import run
from storage.csv_backend import read_clientes, read_vehiculos

def main():
    backend = os.getenv("BACKEND", "csv")  # "mem" o "csv"
    db = {"clientes": [], "vehiculos": []}

    if backend == "csv":
        base = os.getenv("DATA_DIR", "data")
        clientes_path = os.path.join(base, "clientes.csv")
        vehiculos_path = os.path.join(base, "vehiculos.csv")
        db["clientes"] = read_clientes(clientes_path)
        db["vehiculos"] = read_vehiculos(vehiculos_path)
    else:
        # memoria (como en S3)
        db = {"clientes": [], "vehiculos": []}

    run(db)

if __name__ == "__main__":
    main()
