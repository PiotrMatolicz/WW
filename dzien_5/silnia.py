import sys

# Silnia to iloczyn kolejnych liczb naturalnych od 1 do n
# Np. silnia(5) = 1*2*3*4*5 = 120

def silnia(n):
    wynik = 1
    for i in range(1, n+1):
        wynik = wynik * i # albo wynik *= i
    return wynik


# Gdy użyjemy funkcji math.prod, można skrócić zapis:
def silnia_prod(n):
    from math import prod
    return prod(range(1, n+1))


# Informacyjnie, abyście zobaczyli - wersja rekurencyjna
# rekurencja (recursion) to taka sytuacja, że funkcja wywołuje samą siebie:
def silnia_rek(n):
    if n <= 1: return 1
    return silnia_rek(n-1) * n


# program:
# zwiększamy limit długości wypisywanych liczb, aby zobaczyć wyniki większych silnii
sys.set_int_max_str_digits(1_000_000)

while True:
    arg = int(input('Podaj liczbę: '))
    if arg < 0: break # ujemna liczba kończy program
    wynik = silnia(arg)
    print(f'{arg}! = {wynik}')
