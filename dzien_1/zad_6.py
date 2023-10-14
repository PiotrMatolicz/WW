"""
Napisz program, który na podstawie dwóch podanych liczb obliczy wynik zadanej operacji
(dodawanie, odejmowanie, mnożenie, dzielenie). W przypadku podania nieprawidłowej operacji
program ma wyświetlić odpowiedni komunikat o błędzie.

Przykładowy komunikat programu:
Podaj pierwszą liczbę: 10
Podaj drugą liczbę: 5
Podaj rodzaj operacji (+, -, *, /): +
Wynik: 15
"""

liczba_1 = float(input('Podaj pierwszą liczbę: '))
liczba_2 = float(input('Podaj drugą liczbę: '))
operacja = input('Podaj rodzaj operacji (+, -, *, /): ')

if operacja == '+':
    print(f"Wynik: {liczba_1 + liczba_2}")
elif operacja == '-':
    print(f"Wynik: {liczba_1 - liczba_2}")
elif operacja == '*':
    print(f"Wynik: {liczba_1 * liczba_2}")
elif operacja == '/':
    print(f"Wynik: {liczba_1 / liczba_2}")
else:
    print('Nieobslugiwana operacja')
