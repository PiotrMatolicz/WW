def palindrom(napis):
    for i in range(len(napis) // 2):
        if napis[i] != napis[-1 - i]:
            return False
        else:
            return True

while True:
    napis = input('Podaj tekst: \n')
    if not napis: break
    if palindrom(napis):
        print('Jest palindromem')
    else:
        print('Nie jest palindromem')

