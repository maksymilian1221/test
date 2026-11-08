import string


def is_palindrome(text: str) -> bool:
    tekst_czysty = ""
    for znak in text.lower():
        if not znak.isspace():
            tekst_czysty += znak
    return tekst_czysty == tekst_czysty[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Liczba nie może być ujemna!")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for _ in range(2, n + 1):
        kolejna = a + b
        a = b
        b = kolejna
    return b


def count_vowels(text: str) -> int:
    samogloski = "aeiouy"
    licznik = 0
    for litera in text.lower():
        if litera in samogloski:
            licznik += 1
        elif litera in "ąę":
            licznik += 1
    return licznik


def calculate_discount(price: float, discount: float) -> float:
    if discount < 0 or discount > 1:
        raise ValueError("Zniżka musi być między 0 a 1!")

    cena_po_rabacie = price - (price * discount)
    return float(cena_po_rabacie)


def flatten_list(nested_list: list) -> list:
    wynik = []
    for element in nested_list:
        if isinstance(element, list):
            wynik.extend(flatten_list(element))
        else:
            wynik.append(element)
    return wynik


def word_frequencies(text: str) -> dict:
    if not text.strip():
        return {}
    tekst_bez_znakow = ""
    for znak in text.lower():
        if znak not in string.punctuation:
            tekst_bez_znakow += znak

    slowa = tekst_bez_znakow.split()
    statystyka = {}

    for slowo in slowa:
        if slowo in statystyka:
            statystyka[slowo] += 1
        else:
            statystyka[slowo] = 1

    return statystyka


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True