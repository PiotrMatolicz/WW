
def silnia(n):
    wynik = 1
    for x in range(1, n + 1):
        wynik *= x
        return wynik

while True:
    arg= int(input( 'Podaj liczbę: '))
    if arg < 0 : break
    wynik = silnia(arg)
    print(f'{arg} != {wynik}')



