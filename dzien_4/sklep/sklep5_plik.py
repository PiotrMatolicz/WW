PLIK = 'sklep.csv'
ENCODING = 'UTF-8'
cennik = {}
koszt_sumaryczny = 0

menu = '''
Q - zakończ aplikację
R - wczytaj dane z pliku
W - zapisz dane do pliku
P - wypisz dostępne towary
K - kup jakiś produkt
C - dodaj nowy produkt lub zmień cenę
U - usuń towar z cennika
'''

while True:
    print(menu)
    polecenie = input('Wybierz polecenie: ').strip().upper()
    if polecenie == 'Q':
        break
    elif polecenie == 'R':
        with open(PLIK, mode='r', encoding=ENCODING) as plik:
            for linia in plik:
                # to zadziała tylko, jeśli każda linia pliku ma dokładnie dwa pola rozdzielone przecinkiem
                nazwa, cena = linia.split(',')
                cennik[nazwa] = int(cena)
    elif polecenie == 'W':
        with open(PLIK, mode='w', encoding=ENCODING) as plik:
            for nazwa, cena in cennik.items():
                print(nazwa, cena, sep=',', file=plik)
    elif polecenie == 'P':
        print('Dostępne towary')
        for nazwa, cena in cennik.items():
            print(f' * {nazwa} za {cena} zł')
    elif polecenie == 'K':
        nazwa = input('Podaj nazwę wybranego towaru: ')
        try:
            print(f'Jedna sztuka towaru {nazwa} kosztuje {cennik[nazwa]} zł.')
            sztuk = int(input('Ile sztuk chcesz kupić? '))
            koszt = cennik[nazwa] * sztuk
            koszt_sumaryczny += koszt
            print(f'Za {sztuk} sztuk towaru {nazwa} płacisz {koszt} zł.')
        except KeyError:
            print(f'Nie istnieje towar o nazwie {nazwa}')
        except ValueError as e:
            print(f'Błąd: {e}')
    elif polecenie == 'C':
        nazwa = input('Podaj nazwę towaru: ')
        try:
            cena = int(input('Podaj cenę tego towaru: '))
            cennik[nazwa] = cena
        except ValueError as e:
            print(f'Błąd: {e}')
    elif polecenie == 'U':
        nazwa = input('Podaj nazwę towaru: ')
        try:
            del cennik[nazwa]
        except KeyError:
            print(f'Nie istnieje towar o nazwie {nazwa}')
    else:
        print(f'Nieznane polecenie {polecenie}')

print(f'Łącznie suma zakupów: {koszt_sumaryczny} zł')
