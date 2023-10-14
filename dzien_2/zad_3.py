"""
Napisz program wyświetlający minimalną oraz maksymalną liczbę z wszystkich
liczb wprowadzonych liczb przez użytkownika.

Daj użytkownikowi możliwość zakończenia wprowadzania liczb odpowiednią komendą (np. KONIEC).
Zadbaj o obsłużenie przypadku gdy użytkownik nie wprowadzi żadnej liczby.

Jak to zrobimy?
- zdefiniujmy dwie zmienne do trzymania minimum i maximum z wprowadzonych liczb, ale na początku
przypiszemy None
- w nieskończonej pętli while bede wczytywał dane od użytkownika, sprawdzę czy wpisał KONIEC i wtedy przerwę pętlę
- jeśli nie KONIEC, to sprawdzę czy podana liczba jest mniejsza niz minimum, czy jest większa niz maksimum,
  jeśli tak, to przypisze nowe wartości
- jeśli w zmiennej minimum, maksimum jest None, to tez przypisze te wartość
"""

znalezione_min = None
znalezione_max = None

while True:
    dane_wejsciowe = input('Podaj liczbę lub KONIEC: ')
    if dane_wejsciowe == 'KONIEC':
        break

    liczba = float(dane_wejsciowe)

    if znalezione_min is None or liczba < znalezione_min:
        znalezione_min = liczba

    if znalezione_max is None or liczba > znalezione_max:
        znalezione_max = liczba

print(f"Znalezione minimum: {znalezione_min}")
print(f"Znalezione maksimum: {znalezione_max}")
