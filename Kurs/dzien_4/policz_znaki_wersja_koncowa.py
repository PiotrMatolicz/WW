"""
Napisz program zliczający liczbę wystąpień każdego znaku w podanym przez użytkownika napisie.
Dla napisu 'aaabbacd' wynikiem ma być:
a - 4
b - 2
c - 1
d - 1
"""

# W tej wersji napis przeglądamy tylko jeden raz, a ifem sprawdzamy czy to jest pierwsze, czy kolejne wystąpienie.
napis = input('Wprowadź napis:\n')

znaki = {}
for znak in napis:
    if znak in znaki:
        # to jest kolejne wystapienie
        znaki[znak] += 1
    else:
        # to jest pierwsze wystąpienie
        znaki[znak] = 1

for znak, ile in znaki.items():
    print(f'{znak} - {ile:2}')
