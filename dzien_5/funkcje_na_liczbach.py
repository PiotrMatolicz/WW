def max3_v1(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c


# Inny zapis
def max3(a, b, c):
    if a > b and a > c:
        return a
    if b > c:
        return b
    return c


wynik = max3(3, 4, 5)
print('Wynik:', wynik)

# można też wynik bezpośrednio wypisać
print(max3(-5, 13, 13))
print("=" * 30)


def suma(liczby):
    wynik = 0
    for liczba in liczby:
        wynik += liczba
    return wynik


def suma_parzystych(liczby):
    '''Funkcja zwraca sumę tych elementów listy, które są parzyste.'''
    wynik = 0
    for liczba in liczby:
        if liczba % 2 == 0:
            wynik += liczba
    return wynik


print(suma([3, 5, 7]))
print(suma([22, 44, 100, -1, 1]))
lista = [33, 44, 55]
print(suma(lista))

# parametrem tak napisanej funkcji nie musi być lista
print(suma(range(100, 200)))
print(suma(range(1, 11, 2)))

print("=" * 30)

print(suma_parzystych([1, 2, 3, 4, 5]))
print(suma_parzystych([3, 5, 7]))

