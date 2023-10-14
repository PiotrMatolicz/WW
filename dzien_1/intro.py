# to jest komentarz

first_name = 'Piotr'

# Typy danych w Pythonie

# napisy, str
print('Piotr')
print("Piotr")
print('Ksiazka "Pan Tadeusz"')
print("Ksiazka 'Pan Tadeusz'")
print("Ksiazka \"Pan Tadeusz\"")  # eskejpowanie znakow

# standardowo napisy sa jednolinijkowe, ale moze tworzyc napisy wielolinijkowe
print('''Pierwsza linia
Druga linia
Trzecia linia
''')

print("""Pierwsza linia
Druga linia
Trzecia linia
""")

print("Pierwsza linia\nDruga linia\nTrzecia linia")

# liczby całkowite - int
print(10)
print(-1)
print(0)

print(10)
print("10")

print(10 + 10)  # 20
print("10" + "10")  # 1010, konkatenacja

# liczby ułamkowe - float
print(3.14)
print(-0.5)

print(0)
print(0.0)

# liczby zespolone, complex
print(3+5j)

# bool
print(True)
print(False)

# None
# None jest wartością oznaczającą brak wartości
print(None)

print()

# Operatory
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(0.1 * 3)
print(10 // 3)  # dzielenie calkowitoliczbowe
print(10 // 4)
print(10 % 3)  # reszta z dzielenia
print(10 ** 3)  # potegowanie

print("a" + "b")  # konkatenacja
print("x" * 10)
# print("x" * 10.5)  # ERR: TypeError: can't multiply sequence by non-int of type 'float'

# type hinting
last_name: str = 'GG'
last_name = 44
print(last_name)

print('-' * 30)

# Operatory przypisania
liczba = 10
liczba = liczba + 5
print(liczba)

liczba = 10
liczba += 5
print(liczba)

liczba -= 5
print(liczba)

liczba *= 5
print(liczba)

liczba /= 5
print(liczba)

liczba //= 5
print(liczba)

liczba **= 5
print(liczba)

liczba %= 5
print(liczba)

liczba += 1
print(liczba)

# liczba++ - nie ma ++ w pythonie

# Operatory porównania
print(1 == 1)
print(1 == 1.0)
print(0.1 == 0.1)
print(0.3 == 0.1 * 3)
print(1 != 1)
print(1 != 2)
print(1 < 2)
print(1 > 2)
print(1 <= 2)
print(1 >= 2)
print(1 < 1)
print()

# Operatory logiczne
print(not True)
print(not False)
print(False and True)
print(False or True)

print((False or True) and (False or False))

print('-' * 30)

print(bool(10))  # True
print(bool(-10))  # True
print(bool(0))  # False
print(bool(3.14))  # True
print(bool(0.0))  # False
print(bool('Ala ma kota'))  # True
print(bool(''))  # False
print(bool(None))  # False

print('-' * 30)

liczba = 10

if liczba >= 0 and liczba <= 100:
    print('Liczba w zakresie od 0 do 100')
else:
    print('Liczba nie jest w zakresie od 0 do 100')

if 0 <= liczba <= 100:
    print('Liczba w zakresie od 0 do 100')
else:
    print('Liczba nie jest w zakresie od 0 do 100')