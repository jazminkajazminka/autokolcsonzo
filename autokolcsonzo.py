from berles import Berles
from datetime import datetime

class Autokolcsonzo:
    def __init__(self, nev: str):
        self._nev = nev
        self._autok = []
        self._berlesek = []

    def hozzaad_auto(self, auto):
        self._autok.append(auto)

    def hozzaad_berles(self, berles: Berles):
        for b in self._berlesek:
            if b.auto.rendszam == berles.auto.rendszam and b.datum == berles.datum:
                raise Exception("Az autó ezen a napon már foglalt.")
        self._berlesek.append(berles)

    def auto_berlese(self, rendszam: str, datum: str, ugyfel_nev: str):
        auto = next((a for a in self._autok if a.rendszam == rendszam), None)
        if auto is None:
            raise Exception("Nincs ilyen autó.")

        uj_berles = Berles(auto, datum, ugyfel_nev)
        self.hozzaad_berles(uj_berles)
        return auto.berleti_dij

    def berles_lemondasa(self, rendszam: str, datum: str):
        torlendo = None
        for b in self._berlesek:
            if b.auto.rendszam == rendszam and str(b.datum.date()) == datum:
                torlendo = b
        if torlendo:
            self._berlesek.remove(torlendo)
        else:
            raise Exception("Nincs ilyen bérlés.")

    def list_berlesek(self):
        return self._berlesek

    def list_autok(self):
        return self._autok

    def list_kolcsonozheto_autok(self, datum: str):
        try:
            keresett = datetime.strptime(datum, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Hibás dátumformátum (YYYY-MM-DD)")

        foglalt_rendszamok = {
            b.auto.rendszam for b in self._berlesek if b.datum == keresett
        }

        return [auto for auto in self._autok if auto.rendszam not in foglalt_rendszamok]