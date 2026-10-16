# MiTiendaPOS

Proyecto base para un punto de venta de tienda familiar, siguiendo una arquitectura en capas con separación clara entre dominio, servicios, datos y hardware.

## Objetivo

- Registro de ventas con carrito simple
- Base de datos SQLite local
- Generación de ticket en formato ESC/POS
- Soporte de impresora y lector mediante interfaces configurables
- Desarrollo en WSL y despliegue en Ubuntu nativo

## Estructura

```text
MiTiendaPOS/
├── .gitignore
├── README.md
├── pyproject.toml
├── requirements.txt
├── config.example.toml
├── src/
│   └── mitiendapos/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── dominio/
│       │   ├── __init__.py
│       │   ├── producto.py
│       │   ├── carro.py
│       │   └── venta.py
│       ├── servicios/
│       │   ├── __init__.py
│       │   ├── ventas.py
│       │   └── ticket.py
│       ├── datos/
│       │   ├── __init__.py
│       │   ├── repository.py
│       │   └── schema.sql
│       ├── hardware/
│       │   ├── __init__.py
│       │   ├── impresora.py
│       │   └── lector.py
│       └── ui/
│           ├── __init__.py
│           └── caja.py
├── tests/
│   ├── test_carro.py
│   └── test_ticket_dummy.py
└── .venv/
```

## Requisitos

- Python 3.11+
- SQLite
- PySide6 para UI
- python-escpos para impresión térmica
- pytest

## Instalación local

```bash
cd MiTiendaPOS
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## Configuración

Copia el ejemplo:

```bash
cp config.example.toml config.toml
```

Ajusta rutas, tipo de impresora y lector según la máquina.

## Ejecución

```bash
python -m mitiendapos.main
```

## Arquitectura principal

- Dominio: modelos puros sin dependencias de hardware
- Servicios: lógica de venta, descuentos, ticket y cierre
- Datos: repositorio SQLite con transacciones
- Hardware: impresora y lector desacoplados mediante interfaces
- UI: solo consume servicios e informa al usuario
