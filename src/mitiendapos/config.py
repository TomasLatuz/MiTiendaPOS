from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any


DEFAULT_CONFIG_PATH = Path("config.toml")


def load_config(path: str | Path = DEFAULT_CONFIG_PATH) -> dict[str, Any]:
    """Carga la configuración TOML del POS.

    Si el archivo no existe, devuelve un esquema mínimo por defecto.
    """
    config_path = Path(path)
    if not config_path.exists():
        return {
            "impresora": {"tipo": "dummy", "charcode": "CP858"},
            "lector": {"tipo": "teclado"},
            "base_datos": {"ruta": "pos.db"},
            "tienda": {"nombre": "Mi Tienda", "ancho_ticket": 32},
        }

    with config_path.open("rb") as handle:
        return tomllib.load(handle)
