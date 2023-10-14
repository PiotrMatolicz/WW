from datetime import datetime

limit = int(input('Podaj limit: '))

# przy okazji w tym programie zastosujemy technikę pomiaru czasu,
# aby zobaczyć, jak długo działa nasz program; które rozwiązania są bardziej i mniej wydajne
poczatek = datetime.now()

# Wygeneruj listę trójek Pitagorejskich z zakresu od 1 do limit
# a² + b² == c²
# Można zrobić tak, żeby te liczby się nie powtarzały,
# że do listy dodamy tylko takie trójki (a,b,c), że a < b < c <= limit
# przykładowo: [(3,4,5), (5, 12, 13), (6, 8, 10)] .....

# rozwiązanie wyjściowe, które jednak jest dalekie od optymalnego
trojki = [(a, b, c)
             for a in range(1, limit+1)
             for b in range(1, limit+1)
             for c in range(1, limit+1)
             if a < b < c and a**2 + b**2 == c**2]

koniec = datetime.now()
print('Liczba wygenerowanych trójek Pitagorejskich:', len(trojki))
print('Czas generowania:', koniec - poczatek)

if len(trojki) <= 100:
    print(trojki) # żeby nie wypisywać zbyt dużo danych...
else:
    print('Ostatni element:', trojki[-1])
