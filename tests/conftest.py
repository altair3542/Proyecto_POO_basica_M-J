# tests/conftest.py
import os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC  = os.path.join(ROOT, "src")

# Soporta:  from src.models.cliente import Cliente
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Soporta:  from models.cliente import Cliente
if SRC not in sys.path:
    sys.path.insert(0, SRC)
