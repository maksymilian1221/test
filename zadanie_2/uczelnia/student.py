class Student:

    def __init__(self, imie_i_nazwisko: str, oceny: list):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.oceny = oceny

    def czy_zdal(self) -> bool:
        if not self.oceny:
            return False
        srednia = sum(self.oceny) / len(self.oceny)
        return srednia > 50

    def __str__(self):
        srednia = sum(self.oceny) / len(self.oceny) if self.oceny else 0
        return f"Student: {self.imie_i_nazwisko} (Średnia: {srednia:.2f})"