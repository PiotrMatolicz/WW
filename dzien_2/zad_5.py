"""
Napisz program obliczający średnią wartość z 10 podanych przez użytkownika liczb.
Do przechowywania liczb użyj listy.
Skorzystaj z funkcji wbudowanej sum().
"""

liczby = []

while len(liczby) < 10:
    liczba = float(input('Podaj liczbę: '))
    liczby.append(liczba)

srednia = sum(liczby) / len(liczby)
print(f"Średnia z wprowadzonych liczb to {srednia}.")
