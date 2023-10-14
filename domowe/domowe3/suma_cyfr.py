# Type hints - informacja o typie parametrów, wyników i zmiennych
# To jest niezobowiązujące, Python tego nie sprawdza, to jest bardziej dla człowieka (lub dla edytora, np. Pycharm to rozumie).

# podejście "matematyczne"
def suma_cyfr_v1(n:int) -> int:
    assert n >= 0 # gdyby n było ujemne, to dojdzie do wyjątku
    wynik = 0
    while n > 0:
        wynik += n % 10 # ostatnia cyfra
        n //= 10 # dzielenie całkowite, czyli pominięcie ostatniej cyfry
    return wynik


# podejście "techniczne"
def suma_cyfr_v2(n:int) -> int:
    cyfry = str(n)
    wynik = 0
    for cyfra in cyfry:
        wynik += int(cyfra)
    return wynik


# To samo, ale zapis "pajtoniczny"
def suma_cyfr_v3(n:int) -> int:
    return sum(int(cyfra) for cyfra in str(n))


def main():
    while True:
        arg = int(input('Podaj liczbę: '))
        wynik = suma_cyfr_v1(arg)
        print('Suma cyfr v1:', wynik)
        wynik = suma_cyfr_v2(arg)
        print('Suma cyfr v2:', wynik)
        wynik = suma_cyfr_v3(arg)
        print('Suma cyfr v3:', wynik)


if __name__ == '__main__':
    main()
