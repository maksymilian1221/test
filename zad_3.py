def czyParzysta(a: int) -> bool:
    return a % 2 == 0

parzystosc_liczby = czyParzysta(2)

if parzystosc_liczby:
    print(f"Liczba jest liczbą parzystą")
else:
    print(f"Liczba nie jest liczbą parzystą")