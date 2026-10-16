from __future__ import annotations

import sqlite3
from pathlib import Path


class RepositorioSQLite:
    """Repositorio de acceso a SQLite con enfoque de transacción."""

    def __init__(self, db_path: str | Path) -> None:
        self.db_path = str(db_path)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute("PRAGMA journal_mode = WAL")
        return conn

    def _init_db(self) -> None:
        schema_path = Path(__file__).with_name("schema.sql")
        with schema_path.open("r", encoding="utf-8") as handle:
            schema_sql = handle.read()

        with self._connect() as conn:
            conn.executescript(schema_sql)

    def obtener_producto_por_codigo(self, codigo: str):
        with self._connect() as conn:
            row = conn.execute(
                "SELECT id, codigo, nombre, precio, activo FROM productos WHERE codigo = ? AND activo = 1",
                (codigo,),
            ).fetchone()
        if row is None:
            return None
        return {
            "id": row[0],
            "codigo": row[1],
            "nombre": row[2],
            "precio": row[3],
            "activo": bool(row[4]),
        }

    def guardar_venta(self, total: int, medio_pago: str = "efectivo") -> int:
        with self._connect() as conn:
            cursor = conn.execute(
                "INSERT INTO ventas (fecha_hora, total, medio_pago) VALUES (datetime('now'), ?, ?)",
                (total, medio_pago),
            )
            return int(cursor.lastrowid)

    def guardar_detalle_venta(self, venta_id: int, detalle: list[dict]) -> None:
        with self._connect() as conn:
            conn.executemany(
                """
                INSERT INTO detalle_venta
                    (venta_id, producto_id, nombre, cantidad, precio_unitario, descuento_aplicado, subtotal)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        venta_id,
                        item["producto_id"],
                        item["nombre"],
                        item["cantidad"],
                        item["precio_unitario"],
                        item["descuento_aplicado"],
                        item["subtotal"],
                    )
                    for item in detalle
                ],
            )
