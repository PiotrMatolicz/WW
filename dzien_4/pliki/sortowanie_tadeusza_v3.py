import locale

print('Czytam plik...')
with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    linie = wejscie.readlines()
print(f'Wczytałem {len(linie)} linii.')

print('Filtruję...')
linie = [linia.lstrip() for linia in linie if not linia.isspace()]

print('Sortuję...')
locale.setlocale(locale.LC_COLLATE, 'pl_PL')
linie.sort(key=locale.strxfrm)

print('Zapisuję plik...')
with open('posortowany3.txt', mode='w', encoding='UTF-8') as wyjscie:
    wyjscie.writelines(linie)

print('Gotowe')
