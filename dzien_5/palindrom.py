
def palindrom_v1(napis):
    for i in range(len(napis) // 2):
        if napis[i] != napis[-1 - i]:
            return False
    # jeśli przejrzeliśmy wszystkie pozycje i nie znaleźliśmy żadnej niezgodności,
    # to znaczy, że wszystko się zgadzało i można zwrócić True
    return True


def palindrom_v2(napis):
    return napis == napis[::-1]


while True:
    napis = input('Podaj tekst:\n')
    if not napis: break
    if palindrom_v2(napis):
        print('Jest palindromem')
    else:
        print('Nie jest palindromem')