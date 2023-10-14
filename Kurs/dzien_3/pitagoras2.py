from datetime import datetime

limit = int(input('Podaj limit: '))

poczatek = datetime.now()

# Ciekawostka: mnożenie a*a działa w Pythonie znacznie szybciej niż potęgowanie a**2
trojki = [(a, b, c)
             for a in range(1, limit+1)
             for b in range(1, limit+1)
             for c in range(1, limit+1)
             if a < b < c and a*a + b*b == c*c]

koniec = datetime.now()
print('Liczba wygenerowanych trójek Pitagorejskich:', len(trojki))
print('Czas generowania:', koniec - poczatek)

if len(trojki) <= 100:
    print(trojki) # żeby nie wypisywać zbyt dużo danych...
else:
    print('Ostatni element:', trojki[-1])
