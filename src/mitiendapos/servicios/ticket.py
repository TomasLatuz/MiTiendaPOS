from __future__ import annotations


def generar_ticket_bytes(tienda: str, lineas: list[str], ancho: int = 32) -> bytes:
    """Genera un ticket de prueba en texto plano con formato Simple.

    No depende de hardware real; sirve como base para tests y para simular
    impresión en un entorno de desarrollo.
    """
    contenido = [tienda.center(ancho), "-" * ancho]
    contenido.extend(linea[:ancho].ljust(ancho) for linea in lineas)
    contenido.append("-" * ancho)
    contenido.append("Gracias por su compra")
    return "\n".join(contenido).encode("cp858", errors="replace")
