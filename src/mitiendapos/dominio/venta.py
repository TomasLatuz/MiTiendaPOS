from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class DetalleVenta:
    producto_id: int | None
    nombre: str
    cantidad: int
    precio_unitario: int
    descuento_aplicado: int = 0
    subtotal: int = 0


@dataclass
class Venta:
    id: int | None = None
    fecha_hora: datetime | None = None
    total: int = 0
    medio_pago: str = "efectivo"
