R# W tej wersji programu poszczególne operacje (zakupy, zmiana ceny, ...) implementujemy jako oddzielne funkcje.

PLIK = 'sklep.csv'
ENCODING = 'UTF-8'

menu = '''
Q - zakończ aplikację
R - wczytaj dane z pliku
W - zapisz dane do pliku
P - wypisz dostępne towary
K - kup jakiś produkt
C - dodaj nowy produkt lub zmień cenę
U - usuń towar z cennika
'''

cennik = {}
koszt_sumaryczny = 0

def odczytaj_plik():
    with open(PLIK, mode='r', encoding=ENCODING) as plik:
        for linia in plik:
            nazwa, cena = linia.split(',')
            cennik[nazwa] = int(cena)


def zapisz_plik():
    with open(PLIK, mode='w', encoding=ENCODING) as plik:
        for nazwa, cena in cennik.items():
            print(nazwa, cena, sep=',', file=plik)


def wypisz_towary():
    print('Dostępne towary:')
    for nazwa, cena in cennik.items():
        print(f' * {nazwa} za {cena} zł')


def zakupy():
    # Aby funkcja miała prawo modyfikować wartość zmiennej globalnej, deklarujemny tę zmienną jako global
    global koszt_sumaryczny
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


def ustaw_cene():
    nazwa = input('Podaj nazwę towaru: ')
    try:
        cena = int(input('Podaj cenę tego towaru: '))
        cennik[nazwa] = cena
    except ValueError as e:
        print(f'Błąd: {e}')


def usun_towar():
    nazwa = input('Podaj nazwę towaru: ')
    try:
        del cennik[nazwa]
    except KeyError:
        print(f'Nie istnieje towar o nazwie {nazwa}')


def wybierz_z_menu():
    print(menu)
    wybor = input('Wybierz polecenie: ')
    return wybor.strip().upper()


# główna część programu:
while True:
    polecenie = wybierz_z_menu()
    if polecenie == 'Q':
        break
    elif polecenie == 'R':
        odczytaj_plik()
    elif polecenie == 'W':
        zapisz_plik()
    elif polecenie == 'P':
        wypisz_towary()
    elif polecenie == 'K':
        zakupy()
    elif polecenie == 'C':
        ustaw_cene()
    elif polecenie == 'U':
        usun_towar()
    else:
        print(f'Nieznane polecenie {polecenie}')

print(f'Łącznie suma zakupów: {koszt_sumaryczny} zł')
