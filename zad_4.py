def wyswietl_co_drugi(liczby):
    for liczba in liczby[::2]:
        print(liczba)

wyswietl_co_drugi(list(range(1, 11)))