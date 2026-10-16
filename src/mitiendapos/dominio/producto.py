from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Producto:
    codigo: str
    nombre: str
    precio: int
    activo: bool = True
