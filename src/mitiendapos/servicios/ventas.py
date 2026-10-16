from __future__ import annotations

from dataclasses import dataclass

from mitiendapos.dominio.carro import Carro
from mitiendapos.dominio.producto import Producto


@dataclass
class ProductoEncontrado:
    producto: Producto
    descuento_aplicado: int = 0


class ServicioVentas:
    """Lógica de negocio para agregar productos, aplicar descuentos y cerrar ventas."""

    def __init__(self, repositorio) -> None:
        self.repositorio = repositorio
        self.carro = Carro()

    def buscar_producto(self, codigo: str) -> Producto | None:
        registro = self.repositorio.obtener_producto_por_codigo(codigo)
        if registro is None:
            return None
        return Producto(
            codigo=registro["codigo"],
            nombre=registro["nombre"],
            precio=int(registro["precio"]),
            activo=bool(registro["activo"]),
        )

    def agregar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        self.carro.agregar(producto)
        return True

    def confirmar_venta(self, medio_pago: str = "efectivo") -> int:
        if self.carro.cantidad_total == 0:
            raise ValueError("El carrito está vacío")

        venta_id = self.repositorio.guardar_venta(self.carro.total, medio_pago)
        detalle = []
        for item in self.carro.items:
            producto: Producto = item["producto"]
            cantidad = int(item["cantidad"])
            subtotal = producto.precio * cantidad
            detalle.append(
                {
                    "producto_id": None,
                    "nombre": producto.nombre,
                    "cantidad": cantidad,
                    "precio_unitario": producto.precio,
                    "descuento_aplicado": 0,
                    "subtotal": subtotal,
                }
            )
        self.repositorio.guardar_detalle_venta(venta_id, detalle)
        self.carro.limpiar()
        return venta_id
