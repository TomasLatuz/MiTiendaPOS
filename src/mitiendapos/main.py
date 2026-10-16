"""Archivo principal del proyecto.

Este módulo sirve como punto de entrada inicial y dejará la base para
la UI cuando el proyecto avance hacia PySide6.
"""

from __future__ import annotations

from mitiendapos.config import load_config


def main() -> None:
    config = load_config()
    tienda = config.get("tienda", {}).get("nombre", "Mi Tienda")
    print(f"Iniciando {tienda}...")
    print("POS listo para continuar con la implementación de caja.")


if __name__ == "__main__":
    main()
