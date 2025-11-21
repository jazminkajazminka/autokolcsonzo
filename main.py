from autokolcsonzo import Autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles

def elokeszites():
    kolcsonzo = Autokolcsonzo("Car Kft.")

    auto1 = Szemelyauto("AAA-111", "Opel Astra", 10000, 5)
    auto2 = Szemelyauto("BBB-222", "Toyota Corolla", 12000, 5)
    auto3 = Teherauto("CCC-333", "Mercedes Sprinter", 18000, 3500)

    kolcsonzo.hozzaad_auto(auto1)
    kolcsonzo.hozzaad_auto(auto2)
    kolcsonzo.hozzaad_auto(auto3)

    kolcsonzo.hozzaad_berles(Berles(auto1, "2025-11-01", "Kiss Péter"))
    kolcsonzo.hozzaad_berles(Berles(auto1, "2025-11-02", "Nagy Anna"))
    kolcsonzo.hozzaad_berles(Berles(auto2, "2025-11-01", "Kovács Béla"))
    kolcsonzo.hozzaad_berles(Berles(auto3, "2025-11-03", "Fekete Dóra"))

    return kolcsonzo


def menu():
    print("1 - Autó bérlése")
    print("2 - Bérlés lemondása")
    print("3 - Bérlések listázása")
    print("4 - Kölcsönözhető autók listázása adott napra")
    print("5 - Kilépés")


def main():
    kolcsonzo = elokeszites()

    while True:
        menu()
        valasztas = input("Választás: ")

        if valasztas == "1":
            rendszam = input("Rendszám: ")
            datum = input("Dátum (YYYY-MM-DD): ")
            nev = input("Ügyfél neve: ")

            try:
                ar = kolcsonzo.auto_berlese(rendszam, datum, nev)
                print(f"Sikeres bérlés. Ár: {ar} Ft")
            except Exception as e:
                print("Hiba:", e)

        elif valasztas == "2":
            rendszam = input("Rendszám: ")
            datum = input("Dátum: ")

            try:
                kolcsonzo.berles_lemondasa(rendszam, datum)
                print("Bérlés sikeresen lemondva.")
            except Exception as e:
                print("Hiba:", e)

        elif valasztas == "3":
            berlesek = kolcsonzo.list_berlesek()
            for b in berlesek:
                print(b)

        elif valasztas == "4":
            datum = input("Dátum (YYYY-MM-DD): ")
            try:
                szabad_autok = kolcsonzo.list_kolcsonozheto_autok(datum)
                if not szabad_autok:
                    print("Nincs elérhető autó ezen a napon.")
                else:
                    print("Szabad autók:")
                    for auto in szabad_autok:
                        print(auto)
            except Exception as e:
                print("Hiba:", e)

        elif valasztas == "5":
            break

        print()


if __name__ == "__main__":
    main()