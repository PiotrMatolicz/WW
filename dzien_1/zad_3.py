"""
Napisz program obliczający koszt przejazdu z miasta A do B na podstawie podanej
przez użytkownika liczby kilometrów, ceny paliwa oraz spalania.
Zapytaj użytkownika także o nazwy miejscowości.

Jak to policzyć?
koszt = dystans * spalanie / 100.0 * cena_paliwa
koszt = 420 * 5.5 / 100.0 * 4.55

Przykładowe komunikaty programu:
Podaj miasto A: Warszawa
Podaj miasto B: Gdańsk
Podaj dystans Warszawa-Gdańsk: 420
Podaj cenę paliwa: 4.55
Podaj spalanie na 100 km: 5.5
Koszt przejazdu Warszawa-Gdańsk to 105.11 PLN
"""

miasto_a = input('Podaj miasto A: ')
miasto_b = input('Podaj miasto B: ')
dystans = int(input(f"Podaj dystans {miasto_a}-{miasto_b}: "))
cena = float(input('Podaj cenę paliwa: '))
spalanie = float(input('Podaj spalanie na 100 km: '))

koszt = dystans * spalanie / 100.0 * cena

print(f"Koszt przejazdu {miasto_a}-{miasto_b} to {koszt} PLN")
print(f"Koszt przejazdu {miasto_a}-{miasto_b} to {round(koszt)} PLN")
print(f"Koszt przejazdu {miasto_a}-{miasto_b} to {round(koszt, 2)} PLN")

# https://docs.python.org/3/library/string.html#format-specification-mini-language
print(f"Koszt przejazdu {miasto_a}-{miasto_b} to {koszt:_^10.2f} PLN")
