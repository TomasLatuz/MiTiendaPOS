PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL UNIQUE,
    nombre TEXT NOT NULL,
    precio INTEGER NOT NULL,
    activo INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS descuentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_id INTEGER NULL,
    tipo TEXT NOT NULL,
    valor INTEGER NOT NULL,
    desde TEXT,
    hasta TEXT,
    activo INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_hora TEXT NOT NULL,
    total INTEGER NOT NULL,
    medio_pago TEXT NOT NULL DEFAULT 'efectivo'
);

CREATE TABLE IF NOT EXISTS detalle_venta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    venta_id INTEGER NOT NULL,
    producto_id INTEGER NULL,
    nombre TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario INTEGER NOT NULL,
    descuento_aplicado INTEGER NOT NULL DEFAULT 0,
    subtotal INTEGER NOT NULL,
    FOREIGN KEY (venta_id) REFERENCES ventas(id)
);
