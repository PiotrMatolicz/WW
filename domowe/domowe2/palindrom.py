from funkcje import palindrom_v2 as palindrom

while True:
    napis = input('Podaj tekst:\n')
    if not napis: break
    if palindrom(napis):
        print('Jest palindromem')
    else:
        print('Nie jest palindromem')