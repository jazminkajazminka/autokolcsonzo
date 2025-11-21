from auto import Auto


class Teherauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, max_teher: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self._max_teher = max_teher

    @property
    def max_teher(self):
        return self._max_teher

    def __str__(self):
        return f"Teherautó - {self.rendszam}, típus: {self.tipus}, max teher: {self.max_teher} kg, díj: {self.berleti_dij} Ft"