import csv
import os
import sys
import time

PLIK_KOLEJKI = os.path.join(os.path.dirname(__file__), "kolejka.csv")
CZAS_SPRAWDZANIA = 5
CZAS_PRACY = 30


def pobierz_i_zablokuj_zadanie(identyfikator_konsumenta):
    if not os.path.exists(PLIK_KOLEJKI):
        return None

    wiersze = []
    znalezione_zadanie = None

    with open(PLIK_KOLEJKI, mode="r", newline="", encoding="utf-8") as plik:
        czytnik = csv.reader(plik)
        naglowki = next(czytnik, None)
        if naglowki is None:
            return None
        wiersze.append(naglowki)

        for wiersz in czytnik:
            if not wiersz:
                continue
            if wiersz[2] == "pending" and znalezione_zadanie is None:
                wiersz[2] = "in_progress"
                znalezione_zadanie = wiersz
            wiersze.append(wiersz)

    if znalezione_zadanie is not None:
        with open(
            PLIK_KOLEJKI, mode="w", newline="", encoding="utf-8"
        ) as plik:
            pisarz = csv.writer(plik)
            pisarz.writerows(wiersze)

    return znalezione_zadanie


def zakoncz_zadanie(id_zadania):
    if not os.path.exists(PLIK_KOLEJKI):
        return

    wiersze = []
    with open(PLIK_KOLEJKI, mode="r", newline="", encoding="utf-8") as plik:
        czytnik = csv.reader(plik)
        for wiersz in czytnik:
            if wiersz and wiersz[0] == str(id_zadania):
                wiersz[2] = "done"
            wiersze.append(wiersz)

    with open(PLIK_KOLEJKI, mode="w", newline="", encoding="utf-8") as plik:
        pisarz = csv.writer(plik)
        pisarz.writerows(wiersze)


def uruchom_konsumenta(nazwa_operatora):
    print(f"[{nazwa_operatora}] Operator rozpoczął dyżur. Czekam na połączenia...")

    while True:
        zadanie = pobierz_i_zablokuj_zadanie(nazwa_operatora)

        if zadanie:
            id_zadania, nazwa, status, czas = zadanie
            print(f"[{nazwa_operatora}] POBRANO: Zadanie #{id_zadania} ({nazwa}) - status: 'in_progress'")
            print(f"[{nazwa_operatora}] Rozmowa w toku... potrwa {CZAS_PRACY} sekund.")

            time.sleep(CZAS_PRACY)

            zakoncz_zadanie(id_zadania)
            print(f"[{nazwa_operatora}] ZAKOŃCZONO: Zadanie #{id_zadania} obsłużone - status: 'done'")
        else:
            print(f"[{nazwa_operatora}] Brak wolnych zadań. Sprawdzam ponownie za {CZAS_SPRAWDZANIA}s...")
            time.sleep(CZAS_SPRAWDZANIA)


if __name__ == "__main__":
    operator = sys.argv[1] if len(sys.argv) > 1 else "Konsument_1"
    uruchom_konsumenta(operator)