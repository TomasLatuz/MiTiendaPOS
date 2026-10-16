from __future__ import annotations

from collections import defaultdict

from mitiendapos.dominio.producto import Producto


class Carro:
    """Carrito de compra simple para la lógica del POS."""

    def __init__(self) -> None:
        self._items: dict[str, dict[str, object]] = {}

    def agregar(self, producto: Producto, cantidad: int = 1) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")

        item = self._items.get(producto.codigo)
        if item is None:
            self._items[producto.codigo] = {
                "producto": producto,
                "cantidad": cantidad,
            }
            return

        item["cantidad"] = int(item["cantidad"]) + cantidad

    def quitar(self, codigo: str, cantidad: int = 1) -> None:
        if codigo not in self._items:
            return

        item = self._items[codigo]
        nueva_cantidad = int(item["cantidad"]) - cantidad
        if nueva_cantidad <= 0:
            del self._items[codigo]
        else:
            item["cantidad"] = nueva_cantidad

    def limpiar(self) -> None:
        self._items.clear()

    @property
    def items(self) -> list[dict[str, object]]:
        return [
            {"producto": item["producto"], "cantidad": item["cantidad"]}
            for item in self._items.values()
        ]

    @property
    def total(self) -> int:
        subtotal = 0
        for item in self._items.values():
            producto = item["producto"]
            cantidad = int(item["cantidad"])
            subtotal += int(producto.precio) * cantidad
        return subtotal

    @property
    def cantidad_total(self) -> int:
        return sum(int(item["cantidad"]) for item in self._items.values())
