from datetime import datetime

limit = int(input('Podaj limit: '))

poczatek = datetime.now()

# W tej wersji zamiast używać warunku a < b < c, generujemy liczby z takiego zakresu, który ma sens.

# trojki = [(a, b, c)
#              for a in range(1, limit)
#              for b in range(a+1, limit)
#              for c in range(b+1, limit+1)
#              if a*a + b*b == c*c]

trojki = [(a, b, c)
             for c in range(2, limit+1)
             for b in range(1, c)
             for a in range(1, b)
             if a*a + b*b == c*c]

# można jeszcze sprytniej wykorzystując pierwiastek

koniec = datetime.now()
print('Liczba wygenerowanych trójek Pitagorejskich:', len(trojki))
print('Czas generowania:', koniec - poczatek)

if len(trojki) <= 100:
    print(trojki) # żeby nie wypisywać zbyt dużo danych...
else:
    print('Ostatni element:', trojki[-1])
