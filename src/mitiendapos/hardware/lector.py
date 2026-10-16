from __future__ import annotations

from abc import ABC, abstractmethod


class LectorCodigos(ABC):
    @abstractmethod
    def leer(self) -> str:
        raise NotImplementedError


class LectorTeclado(LectorCodigos):
    def leer(self) -> str:
        return input("Ingrese código: ")


class LectorSimulado(LectorCodigos):
    def __init__(self, codigos: list[str] | None = None) -> None:
        self.codigos = codigos or []
        self.indice = 0

    def leer(self) -> str:
        if self.indice >= len(self.codigos):
            raise RuntimeError("No hay más códigos simulados")
        codigo = self.codigos[self.indice]
        self.indice += 1
        return codigo


def crear_lector(tipo: str, **kwargs) -> LectorCodigos:
    if tipo == "teclado":
        return LectorTeclado()
    if tipo == "simulado":
        return LectorSimulado(kwargs.get("codigos", []))
    raise ValueError(f"Tipo de lector no soportado: {tipo}")
