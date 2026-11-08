import magazine.utils

class Produkt:
    def __init__(self, nazwa: str, cena: float):
        self.nazwa = nazwa
        self.cena = cena

    def pobierz_informacje(self) -> str:
        sformatowanie = magazine.utils.sformatuj_cene(self.cena)
        return f"Produkt: {self.nazwa}, Cena: {sformatowanie}"