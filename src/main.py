from __future__ import annotations
import argparse
from pathlib import Path
from .controllers.menu import AppConfig, MenuCLI

def _project_root() -> Path:
    # src/ -> project root
    return Path(__file__).resolve().parent.parent

def main() -> None:
    parser = argparse.ArgumentParser(description="Gestor CLI (stub) — MVC + JSON/CSV")
    parser.add_argument("--backend", choices=["csv","json"], default="csv", help="Backend de persistencia (órdenes usan JSON)")
    args = parser.parse_args()

    root = _project_root()
    cfg = AppConfig(data_dir=root / "data", backend=args.backend)
    MenuCLI(cfg).run()

if __name__ == "__main__":
    main()
