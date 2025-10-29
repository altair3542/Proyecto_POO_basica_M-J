# src/views/console.py
from __future__ import annotations
from typing import Iterable, Sequence

def format_title(text: str) -> str:
    line = "=" * max(12, len(text))
    return f"{line}\n{text}\n{line}"

def format_error(msg: str) -> str:
    return f"[ERROR] {msg}"

def format_success(msg: str) -> str:
    return f"[OK] {msg}"

def format_table(headers: Sequence[str], rows: Iterable[Sequence[object]]) -> str:
    # Convierte todo a str y calcula anchos
    rows_str = [[str(c) for c in row] for row in rows]
    headers_str = [str(h) for h in headers]
    widths = [len(h) for h in headers_str]
    for row in rows_str:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))
    # Construir líneas
    def fmt_row(r): return " | ".join(cell.ljust(widths[i]) for i, cell in enumerate(r))
    sep = "-+-".join("-" * w for w in widths)
    out = [fmt_row(headers_str), sep]
    for r in rows_str:
        out.append(fmt_row(r))
    return "\n".join(out)

def emit(text: str, printer=print) -> None:
    printer(text)
