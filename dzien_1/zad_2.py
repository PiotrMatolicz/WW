"""
Napisz program wypisujący na konsolę Twoje imię i wzrost.
Do przechowywania informacji o Twoim imieniu i wzroście użyj zmiennych.
Do pobierania danych wykorzystaj funkcję input.

Przykładowy komunikat programu:
Imię: Jan
Wzrost: 180
"""

imie = input('Podaj imię: ')
wzrost = int(input('Podaj wzorst: '))

"""
Używam print z dwoma argumentami. Przecinek oddziela argumenty funkcji.
"""
print('Imię:', imie)
print('Wzrost:', wzrost)

"""
Do funkcji print przekazuję jeden argument, który jest wynikiem łączenia dwóch stringów.
"""
print('Imię: ' + imie)
print('Wzrost: ' + str(wzrost))

a = 1
b = 2
c = 'Krysia'
print('Zmienna a = ' + str(a) + ', a b to się równa ' + str(b) + " a w c mamy " + c)
# Zmienna a = 1, a b to się równa 2 a w c mamy Krysia

print(f"Zmienna a = {a}, a b to się równa {b} a w c mamy {c}, {a + b}")
# Zmienna a = 1, a b to się równa 2 a w c mamy Krysia
