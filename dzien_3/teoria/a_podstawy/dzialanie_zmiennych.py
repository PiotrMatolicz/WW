# To jest komentarz

# W Pythonie próba odczytania niezdefiniowanej zmiennej jest błędem:
# print(zmienna)  # błąd

# Zmienne są tworzone w ten sposób, że pod jakąś nazwę wpisuje się wartość
imie = 'Ala'
liczba = 15
x = 2*liczba
pi = 3.14

# Teraz te zmienne już istnieją
print(imie, liczba, pi)
print('x = ', x)

# Do zmiennej można wpisać inną wartość
imie = 'Alicja'
liczba = 100
print(imie, liczba)
print('x = ', x) # nadal 30

# Do sprawdzenia typu można użyć operacji type:
print('Zmienna liczba jest teraz typu', type(liczba), 'i ma wartosc', liczba)

# O ile w Javie lub C takie rzeczy by nie przeszły,
# to w Pythonie do istniejącej zmiennej można wpisać wartość innego typu niż była wcześniej

liczba = 'Ala ma kota'
print(liczba)

print('Zmienna liczba jest teraz typu', type(liczba), 'i ma wartosc', liczba)

# Nie trzeba tego robić i zazwyczaj się nie robi,
# ale istnieje instrukcja del, która usuwa zmienne
del liczba
# print(liczba) # błąd


