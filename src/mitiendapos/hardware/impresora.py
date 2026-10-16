from __future__ import annotations

from abc import ABC, abstractmethod


class ImpresoraBase(ABC):
    @abstractmethod
    def imprimir(self, contenido: bytes) -> None:
        raise NotImplementedError


class ImpresoraDummy(ImpresoraBase):
    def __init__(self) -> None:
        self.output: bytearray = bytearray()

    def imprimir(self, contenido: bytes) -> None:
        self.output.extend(contenido)


class ImpresoraArchivo(ImpresoraBase):
    def __init__(self, ruta: str) -> None:
        self.ruta = ruta

    def imprimir(self, contenido: bytes) -> None:
        with open(self.ruta, "wb") as archivo:
            archivo.write(contenido)


def crear_impresora(tipo: str, **kwargs) -> ImpresoraBase:
    if tipo == "dummy":
        return ImpresoraDummy()
    if tipo == "archivo":
        return ImpresoraArchivo(kwargs.get("ruta", "/tmp/ticket.bin"))
    raise ValueError(f"Tipo de impresora no soportado: {tipo}")
