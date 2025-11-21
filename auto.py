from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int):
        self._rendszam = rendszam
        self._tipus = tipus
        self._berleti_dij = berleti_dij

    @property
    def rendszam(self):
        return self._rendszam

    @property
    def tipus(self):
        return self._tipus

    @property
    def berleti_dij(self):
        return self._berleti_dij

    @abstractmethod
    def __str__(self):
        pass