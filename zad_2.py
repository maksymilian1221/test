# pętla for
def pomnoz_for(liczby):
    wynik = []
    for liczba in liczby:
        wynik.append(liczba * 2)
    return wynik

# lista składana
def pomnoz_comprehension(liczby):
    return [liczba * 2 for liczba in liczby]

lista_liczb = [1, 2, 3, 4, 5]
print(pomnoz_for(lista_liczb))
print(pomnoz_comprehension(lista_liczb))