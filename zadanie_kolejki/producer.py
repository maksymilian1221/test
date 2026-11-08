import csv
import os
import sys
import time

PLIK_KOLEJKI = os.path.join(os.path.dirname(__file__), "kolejka.csv")
NAGLOWKI = ["id", "nazwa_zadania", "status", "utworzono"]


def inicjalizuj_plik():
    if not os.path.exists(PLIK_KOLEJKI):
        with open(
            PLIK_KOLEJKI, mode="w", newline="", encoding="utf-8"
        ) as plik:
            pisarz = csv.writer(plik)
            pisarz.writerow(NAGLOWKI)


def pobierz_nastepne_id():
    if not os.path.exists(PLIK_KOLEJKI):
        return 1

    with open(PLIK_KOLEJKI, mode="r", newline="", encoding="utf-8") as plik:
        czytnik = list(csv.reader(plik))
        if len(czytnik) <= 1:
            return 1
        ostatni_wiersz = czytnik[-1]
        try:
            return int(ostatni_wiersz[0]) + 1
        except ValueError:
            return 1


def dodaj_zadanie():
    inicjalizuj_plik()
    nowe_id = pobierz_nastepne_id()
    nazwa = f"Rozmowa_z_klientem_{nowe_id}"
    status = "pending"
    czas_dodania = time.strftime("%Y-%m-%d %H:%M:%S")

    with open(PLIK_KOLEJKI, mode="a", newline="", encoding="utf-8") as plik:
        pisarz = csv.writer(plik)
        pisarz.writerow([nowe_id, nazwa, status, czas_dodania])

    print(f"[PRODUCER] Zarejestrowano zadanie: #{nowe_id} ({nazwa}) ze statusem '{status}'")


if __name__ == "__main__":
    liczba_zadan = 1
    if len(sys.argv) > 1:
        try:
            liczba_zadan = int(sys.argv[1])
        except ValueError:
            liczba_zadan = 1

    for _ in range(liczba_zadan):
        dodaj_zadanie()