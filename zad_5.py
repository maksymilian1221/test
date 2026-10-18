def czy_znajduje_sie(lista: list, a: int) -> bool:
    return a in lista

test = czy_znajduje_sie([1,2,3,4,5], 4)
print(test)