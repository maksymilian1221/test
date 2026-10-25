class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"DOM: {self.address} | Powierzchnia: {self.area}m2 | Pokoje: {self.rooms} | Działka: {self.plot}m2 | Cena: {self.price} PLN"


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"MIESZKANIE: {self.address} | Piętro: {self.floor} | Powierzchnia: {self.area}m2 | Pokoje: {self.rooms} | Cena: {self.price} PLN"


if __name__ == "__main__":
    my_house = House(
        area=150.5, rooms=5, price=1200000, address="Kwiatowa 10, Poznań", plot=800
    )
    my_flat = Flat(
        area=65.0, rooms=3, price=650000, address="Mickiewicza 5/12, Kraków", floor=3
    )

    print(my_house)
    print(my_flat)
