"""
Napisz program zliczający liczbę znaków w podanym przez użytkownika napisie
pomiędzy nawiasami <>. Nawiasy mogą wystąpić tylko raz.

Przykład:
Ala ma <kota>, a kot ma Alę
4


1. Sprawdzam liczbę < i > - powinno ich być po jednym,
      jeżeli liczba tych nawiasów jest inna, to kończę program
2. W pętli sprawdzam, czy:
      - mam zliczać
      - mam przestać zliczać
      - czy zliczanie jest włączone i wtedy zliczam,
"""
napis = input('Podaj napis: ')

# if napis.count('<') != 1 or napis.count('>') != 1 or napis.index('<') > napis.index('>'):
if napis.count('<') != 1 or napis.count('>') != 1 or not (napis.index('<') < napis.index('>')):
    print('Nieprawidlowy napis.')
    exit()

czy_zliczac = False
liczba_znakow = 0

for litera in napis:
    if litera == '<':
        czy_zliczac = True
    elif litera == '>':
        czy_zliczac = False
    elif czy_zliczac is True:
        liczba_znakow += 1

print(f"Dla napisu '{napis}' znaleziono {liczba_znakow} znaków.")
