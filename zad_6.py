def laczenie_list(lista1:list, lista2:list) -> list:
    lista3 = lista1 + lista2
    lista4 = []
    lista5 = []
    for a in lista3:
        if a not in lista4:
            lista4.append(a)
    lista5 = [x**3 for x in lista4]
    return lista5

dzialanie = laczenie_list([1,2,3,4,5],[5,6,7,8,9])

print(dzialanie)