# Względem wersji 3:
# * przechowywanie danych w pliku
# + operacje odczytu i zapisu pliku

menu = '''
 Q - zakończ program
 P - wypisz dostępne towary
 R - wczytaj dane z pliku
 W - zapisz dane do pliku
 K - wykonaj zakupy
 N - zdefiniuj nowy towar
 U - usuń towar z cennika
 C - zmień cenę towaru
 D - dostawa towaru'''

SEP = ';'
PLIK = 'towary.csv'

towary = {}

print('Witamy w naszym sklepie')
while True:
    print(menu)
    akcja = input('Wybierz polecenie: ').strip().upper()
    if akcja == 'Q':
        break
    elif akcja == 'P':
        print('Dostępne produkty:')
        print(f'| {"nazwa":19}|{" cena":6} |{" ilość":6} |')
        print('=' * 38)
        for nazwa, (cena, ilosc) in towary.items():
            print(f'| {nazwa:19}|{cena:6} |{ilosc:6} |')
    elif akcja == 'R':
        with open(PLIK, 'r') as plik:
            towary = {}
            ile = 0
            for linia in plik:
                nazwa, cena, ilosc = linia.strip().split(SEP)
                towary[nazwa] = [int(cena), int(ilosc)]
                ile += 1
            print(f'Wczytano dane {ile} towarów')
    elif akcja == 'W':
        with open(PLIK, 'w') as plik:
            ile = 0
            for nazwa, (cena, ilosc) in towary.items():
                print(nazwa, cena, ilosc, sep=SEP, file=plik)
                ile += 1
            print(f'Zapisano dane {ile} towarów')
    elif akcja == 'K':
        suma = 0
        while True:
            nazwa = input('Podaj nazwę towaru lub naciśnij Enter, aby zakończyć: ')
            if not nazwa:
                break
            if nazwa not in towary:
                print(f'Nieznany towar {nazwa}')
                continue
            sztuki = int(input('Ile sztuk? '))
            if sztuki > towary[nazwa][1]:
                print(f'Nie ma tylu sztuk towaru. Jest tylko {towary[nazwa][1]}.')
                continue
            do_zaplaty = towary[nazwa][0] * sztuki
            towary[nazwa][1] -= sztuki
            print(f'Za {sztuki} sztuk towaru {nazwa} do zapłaty będzie {do_zaplaty}')
            suma += do_zaplaty
        print(f'Łącznie za cały koszyk do zapłaty: {suma}')
    elif akcja == 'N':
        nazwa = input('Podaj nazwę nowego towaru: ')
        if nazwa in towary:
            print('Taki towar już istnieje, przerywam')
            continue
        cena = int(input('Podaj cenę towaru: '))
        towary[nazwa] = [cena, 0]
    elif akcja == 'C':
        nazwa = input('Podaj nazwę istniejącego towaru: ')
        if nazwa not in towary:
            print('Taki towar nie istnieje, przerywam')
            continue
        print(f'Obecna cena: {towary[nazwa][0]}')
        cena = int(input('Podaj nową cenę towaru: '))
        towary[nazwa][0] = cena
    elif akcja == 'U':
        nazwa = input('Podaj nazwę istniejącego towaru: ')
        if nazwa not in towary:
            print('Taki towar nie istnieje, przerywam')
            continue
        del towary[nazwa]
        print('Towar usunięty')
    elif akcja == 'D':
        nazwa = input('Podaj nazwę istniejącego towaru: ')
        if nazwa not in towary:
            print('Taki towar nie istnieje, przerywam')
            continue
        print(f'Obecny stan magazynowy: {towary[nazwa][1]}')
        zmiana = int(input('Podaj liczbę sztuk w dostawie: '))
        towary[nazwa][1] += zmiana
    else:
        print('Nieznane polecenie')

print('Do widzenia')
