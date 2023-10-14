# Aby posortować dane, musimy mieć je wszystkie na raz w pamięci,
# najlepiej w formie listy. Dlatego wczytamy wszystkie linie za pomocą readlines.

print('Czytam plik...')
with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    linie = wejscie.readlines()
print(f'Wczytałem {len(linie)} linii.')

# W tej wersji sortujemy napisy z wykorzystaniem dodatkowych możliwości Pythona, aby uzyskać kolejność alfabetyczną
# zgodną z językiem polskim (lub analogicznie - z dowolnym innym językiem).
# Należy:
# 1) za pomocą setlocale ustawić odpowiedni język
# 2) do funkcji sort przekazać parametr key równy locale.strxfrm

import locale
print('LC_COLLATE przed ustawieniem:', locale.getlocale(locale.LC_COLLATE))

locale.setlocale(locale.LC_COLLATE, '')
print('LC_COLLATE systemowe:', locale.getlocale(locale.LC_COLLATE))

locale.setlocale(locale.LC_COLLATE, 'pl_PL.utf8')
print('LC_COLLATE nasze:', locale.getlocale(locale.LC_COLLATE))

# Możliwości ustawiania lokali:
# - zamiast LC_COLLATE można też wpisać LC_ALL - ustawia podany język we wszystkich kategoriach
# - jako drugi parametr można też przekazać pusty napis ''
#   co spowoduje ustawienie tego języka, który mamy ustawiony w systemie.

print('Sortuję...')
linie.sort(key=locale.strxfrm)

print('Zapisuję plik...')
with open('posortowany2.txt', mode='w', encoding='UTF-8') as wyjscie:
    wyjscie.writelines(linie)

print('Gotowe')
