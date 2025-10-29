# src/main.py
from controllers.menu import run

def main():
    db = {"clientes": [], "vehiculos": []}  # backend en memoria (S3)
    run(db)  # CLI interactivo

if __name__ == "__main__":
    main()
