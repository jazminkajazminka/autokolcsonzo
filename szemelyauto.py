from auto import Auto


class Szemelyauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, ajtok_szama: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self._ajtok_szama = ajtok_szama

    @property
    def ajtok_szama(self):
        return self._ajtok_szama

    def __str__(self):
        return f"Személyautó - {self.rendszam}, típus: {self.tipus}, ajtók: {self.ajtok_szama}, díj: {self.berleti_dij} Ft"