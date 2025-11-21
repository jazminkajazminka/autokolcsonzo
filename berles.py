from datetime import datetime

class Berles:
    def __init__(self, auto, datum: str, ugyfel_nev: str):
        self._auto = auto
        self._datum = self._validate_date(datum)
        self._ugyfel_nev = ugyfel_nev

    @staticmethod
    def _validate_date(datum: str):
        try:
            return datetime.strptime(datum, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Hibás dátumformátum. Használj: YYYY-MM-DD")

    @property
    def auto(self):
        return self._auto

    @property
    def datum(self):
        return self._datum

    @property
    def ugyfel_nev(self):
        return self._ugyfel_nev

    def __str__(self):
        return f"{self.ugyfel_nev} - {self.auto.rendszam} - {self.datum.date()}"