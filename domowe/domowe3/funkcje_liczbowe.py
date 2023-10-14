# Definicje funkcji w różnych wersjach.
# Niektóre (fib_rek oraz czy_pierwsza 1 i 2) są mało wydajne, ale mimo wszystko warto takie definicje zobaczyć.

# wersja "matematyczna"
def suma_cyfr_v1(n):
    wynik = 0
    if n < 0:
        n = -n
    while n != 0:
        wynik += n % 10
        n //= 10
    return wynik

# wersja "techniczna"
def suma_cyfr_v2(n):
    cyfry = str(abs(n))
    wynik = 0
    for cyfra in cyfry:
        wynik += int(cyfra)
    return wynik


# wersja "techniczna" ze skrótowym zapisem typu comprehension
def suma_cyfr_v3(n):
    return sum(int(cyfra) for cyfra in str(abs(n)))


# wersja "techniczna" ze skrótowym zapisem `map`
def suma_cyfr_v4(n):
    return sum(map(int, str(abs(n))))


def silnia_rek(n):
    if n <= 1: return 1
    return n * silnia_rek(n-1)


def silnia(n):
    iloczyn = 1
    for i in range(1, n+1):
        iloczyn *= i
    return iloczyn


def fib_rek(n):
    if n <= 1: return n
    return fib_rek(n-2) + fib_rek(n-1)


def fib_tab(n):
    tab = [0, 1]
    for i in range(2, n+1):
        tab.append(tab[-1] + tab[-2])
    return tab[n]


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = a+b, a
    return a


def czy_pierwsza_1(n):
    dzielniki = list()
    for i in range(1, n+1):
        if n % i == 0:
            dzielniki.append(i)
    # teraz mamy wszystkie dzielniki:
    # print(dzielniki)
    # liczba naturalna jest liczbą pierwszą wtedy i tylko wtedy, gdy posiada dwa dzielniki naturalne
    return len(dzielniki) == 2


def czy_pierwsza_2(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def czy_pierwsza_3(n):
    from math import sqrt
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n+1))+1):
        if n % i == 0:
            return False
    return True


def czy_pierwsza_4(n):
    from math import sqrt
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n+1))+1, 2):
        if n % i == 0:
            return False
    return True


def main():
    # Testy funkcji dla przykładowych wartości
    for x in [0, 1, 7, 17, 123, -123, 543210, 10101010, 192837]:
        print(f'suma cyfr {x} v1 = {suma_cyfr_v1(x)}')
        print(f'suma cyfr {x} v2 = {suma_cyfr_v2(x)}')
        print(f'suma cyfr {x} v3 = {suma_cyfr_v3(x)}')
        print(f'suma cyfr {x} v4 = {suma_cyfr_v4(x)}')
    print()
    for x in list(range(0, 21)) + [100, 200]:
        print(f'silniaR({x}) = {silnia_rek(x)}')
        print(f'silnia ({x}) = {silnia(x)}')
    print()

    for x in list(range(0, 21)) + [40]:
        print(f'fibR({x}) = {fib_rek(x)}')
        print(f'fibT({x}) = {fib_tab(x)}')
        print(f'fib ({x}) = {fib(x)}')
    for x in [50, 100, 200, 500, 1000]:
        print(f'fibT({x}) = {fib_tab(x)}')
        print(f'fib ({x}) = {fib(x)}')
    print()
    for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 19, 99, 100, 101, 169052003, 2147483647]:
        print(f'pierwsza v1 {x} = {czy_pierwsza_1(x)}')
        print(f'pierwsza v2 {x} = {czy_pierwsza_2(x)}')
        print(f'pierwsza v3 {x} = {czy_pierwsza_3(x)}')
        print(f'pierwsza v4 {x} = {czy_pierwsza_4(x)}')
    print()


if __name__ == '__main__':
    main()
