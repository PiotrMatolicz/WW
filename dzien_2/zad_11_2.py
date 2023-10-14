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

list_1 = napis.split('<')
list_2 = list_1[1].split('>')
napis_new = list_2[0]
print(f'W napisie "{napis}" jest {len(napis_new)} znaków między < i >')
