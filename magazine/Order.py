import magazine.utils

class Zamowienie:
    def __init__(self, numer_zamowienia: int):
        self.numer_zamowienia = numer_zamowienia
        self.lista_produktow = []

    def wyswietl_podsumowanie(self) -> str:
        return f"Zamówienie nr {self.numer_zamowienia}, liczba pozycji: {len(self.lista_produktow)}"