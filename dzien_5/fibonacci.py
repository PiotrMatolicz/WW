'''
Zwraca n-tą liczbę Fibonacciego, gdzie liczby Fibonacciego są zdefiniowane następująco:
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-2) + fib(n-1)
Co oznacza, że początkowe liczby Fibonacciego to: 0 1 1 2 3 5 8 13 21 34 55
Kolejna liczba jest sumą dwóch poprzednich
'''

# Wersja z rekurencją ma wykładniczą złożoność obliczeniową. Spróbuj uruchomić dla argumentów rzędu 35-40...
def fib_rek(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib_rek(n-2) + fib_rek(n-1)


# Obliczanie Fibonacciego za pomocą dwóch zwykłych zmiennych
# Wersja, jak w języku C czy Java, z pomocniczą zmienną "nowa"
def fib1(n):
    biezaca = 0
    poprzednia = 1
    for i in range(n):
        nowa = biezaca + poprzednia
        poprzednia = biezaca
        biezaca = nowa
    return biezaca

# Wersja "Pajtoniczna" bez pomocniczej zmiennej:
def fib(n):
    biezaca, poprzednia = 0, 1
    for _ in range(n):
        biezaca, poprzednia = biezaca + poprzednia, biezaca
    return biezaca


while True:
    arg = int(input('Podaj liczbę: '))
    if arg < 0: break # ujemna liczba kończy program
    wynik = fib(arg)
    print(f'F({arg}) = {wynik}')
