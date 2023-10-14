from policz_znaki import policz_znaki

while True:
    napis = input('Podaj tekst:\n')
    if not napis: break
    wybor = input('Czy chcesz wprowadzić inne symbole ograniczające? [T/N] ').upper()
    if wybor == 'T':
        poczatek = input('Podaj symbol początkowy: ').strip()
        koniec = input('Podaj symbol końcowy: ').strip()
        wynik = policz_znaki(napis, poczatek, koniec)
    else:
        wynik = policz_znaki(napis)
    print('Wynik:', wynik)
