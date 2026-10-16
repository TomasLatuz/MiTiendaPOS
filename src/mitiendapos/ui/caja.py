from __future__ import annotations


class CajaView:
    """Placeholder para la vista de caja con PySide6."""

    def __init__(self, servicio_ventas=None) -> None:
        self.servicio_ventas = servicio_ventas

    def mostrar_total(self) -> int:
        if self.servicio_ventas is None:
            return 0
        return self.servicio_ventas.carro.total
