licznik = 0
while licznik < 10:
    print(f'{licznik} - Ala ma kota')
    licznik += 1

print('Poza pętlą')

print('-' * 30)

"""
Tuple, krotki - ang. tuple

"""
#       0   1   2
dane = (10, 20, 30)
print(dane)
print(type(dane))

print(dane[0])
print(dane[2])
# print(dane[10])  # ERR IndexError: tuple index out of range

print('-' * 30)

#       0       1                2
dane = ((1, 2), ('a', 'b', 'c'), (True, False))
#        0  1    0    1    2      0     1
print(dane[1][2])

print('-' * 30)

"""
Indeksowanie
- klucze od 0
- klucze ujemne

[start:stop:krok]
- start, stop, krok są opcjonalne
- krok może być dodatni lub ujemny
"""

#       0    1    2    3    4    5    6    7    8    9
dane = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
#       -10  -9   -8   -7   -6   -5   -4   -3   -2   -1
print(dane[3])
print(dane[-1])
print(dane[-7])
print(dane[len(dane) - 1])
print(dane[-1])

#       0    1    2    3    4    5    6    7    8    9
dane = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
#       -10  -9   -8   -7   -6   -5   -4   -3   -2   -1
print(dane[0:3])  # przedział lewostronnie domknięty, prawostronnie otwarty
print(dane[3:6])
print(dane[1:-1])
print(dane[1:])
print(dane[:4])
print(dane[:])
print(dane[::2])
print(dane[::3])
print(dane[::-1])
print(dane[::-2])

print(len(dane))
print('b' in dane)
print('x' in dane)
print('b' not in dane)

liczby = (1, 2, 3, 4, 5)
print(min(liczby))
print(max(liczby))
print(sum(liczby))
print(liczby * 2)
#       0    1    2
dane = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(dane.index('c'))  # 2
print(dane.count('c'))
# dane[0] = 'A'  # ERR: TypeError: 'tuple' object does not support item assignment

print('-' * 30)

"""
Listy, ang. list
- operator dostępu [] działa dokładnie tak samo
"""
#       0   1   2   3   4   5   6   7   8   10
dane = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(dane)
print(type(dane))

dane[0] = 11
print(dane)

dane.append(110)
print(dane)

dane.extend([120, 130, 140])
print(dane)

dane[0:3] = [-1, -2, -3]
print(dane)

del(dane[0])
print(dane)

dane.sort(reverse=True)
print(dane)

print('-' * 30)

dane = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

licznik = 0
while licznik < len(dane):
    liczba = dane[licznik]
    print(liczba)
    licznik += 1

print('-' * 5)

for liczba in dane:
    print(liczba)

print('-' * 30)

imiona = ('Piotr', 'Ala', 'Tomek', 'Krysia')
for imie in imiona:
    print(imie)

print('-' * 30)

# pozwala iterowac po obiektach iterowalnych
# czyli takich, które są "iterable".
for liczba in range(2, 11, 2):
    print(liczba)

print('-' * 30)

print("Ala", "Ola", sep='|')
print("Tomek", "Piotr", sep="#")

print('-' * 30)

print('Ala', end='')
print('Ola')

print('-' * 30)

print(f"...{10:<5}...")
print(f"...{10:5}...")
print(f"...{10:^5}...")

print('-' * 30)

import random

print(random.randint(1, 100))

print('-' * 30)

napis = 'Ala ma kota a kot ma kompilator'

for litera in napis:
    print(litera)

print('-' * 5)

print(napis[0])
print(napis[0:3])
print(napis[-1])
print(napis[::-1])

print(napis.lower())
print(napis.upper())
print(napis.title())
print(napis.capitalize())

# dzielenie napisu
print(napis.split())
print(napis.split('a'))

# łączenie napisu
napisy = ['a', 'b', 'c']
polaczony_napis = '-'.join(napisy)
print(polaczony_napis)

print(napis.count('a'))
print(napis.index('a'))  # rzuca wyjątkiem jak nie znajdzie
print(napis.find('a'))  # zwraca -1 jak nie znajdzie
print(napis.replace('a', 'X'))

