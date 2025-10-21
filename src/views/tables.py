from __future__ import annotations
from typing import List, Dict, Iterable

def format_table(rows: List[Dict[str, str]], columns: list[str], headers: list[str]) -> str:
    """Construye una tabla en texto sin dependencias."""
    widths = [max(len(str(h)), *(len(str(r.get(c, ""))) for r in rows)) for c, h in zip(columns, headers)]
    def fmt_row(values: Iterable[str]) -> str:
        return " | ".join(str(v).ljust(w) for v, w in zip(values, widths))
    sep = "-+-".join("-" * w for w in widths)
    lines = [fmt_row(headers), sep]
    for r in rows:
        lines.append(fmt_row([r.get(c, "") for c in columns]))
    return "\n".join(lines)

def message_info(text: str) -> str:
    return f"[INFO] {text}"
