# defaultdict działa jak słownik, ale w przypadku próby odczytu wartości z nieistniejącego klucza
# wstawia wartość domyślną (tutaj jest to domyślny int, czyli zero)
from collections import defaultdict

def wiecej_niz(napis, liczba):
    slownik = defaultdict(int)
    for znak in napis:
        slownik[znak] += 1
    return {znak for znak, ile in slownik.items() if ile > liczba}


wynik = wiecej_niz('ala ma kota a kot ma ale', 3)
print(wynik)
