"""
Napisz program obliczający kwadrat 100 pierwszych liczb całkowitych
i wypisujący wyniki na konsolę.

Przykładowe uruchomienie programu:
...
Kwadrat liczby 10 to 100
...
"""

liczba = 1
while liczba <= 100:
    print(f"Kwadrat liczby {liczba} to {liczba ** 2}")
    liczba += 1
