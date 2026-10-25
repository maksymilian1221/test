def wyswietl_parzyste(liczby):
    for liczba in liczby:
        if liczba % 2 == 0:
            print(liczba)


wyswietl_parzyste(list(range(1, 11)))
