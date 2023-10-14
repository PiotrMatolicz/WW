# Przykładowe towary dostępne od razu po starcie aplikacji:
cennik = {
    'pralka': 2300,
    'odkurzacz': 400,
    'telewizor': 1900,
}

# Program w pętli nieskończonej pyta użytkownika, co chce zrobić.
# Użytkownik wybiera jedno z poleceń wpisując wybraną literę.
menu = '''
Q - zakończ aplikację
P - wypisz dostępne towary
K - kup jakiś produkt
C - dodaj nowy produkt lub zmień cenę
U - usuń towar z cennika
'''

koszt_sumaryczny = 0

while True:
    print(menu)
    polecenie = input('Wybierz polecenie: ').strip().upper()
    if polecenie == 'Q':
        break
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

# W tej wersji obsługa błędów jest zapisana w stylu "ofensywnym":
# próbujemy wykonać operacje nawet, jeśli miałbyby skończyć się wyjątkiem,
# ale te wyjątki obsługujemy za pomocą try / except.
# Obsługuję nie tylko błędy braku klucza, ale także błędy konwersji tekstu do liczby (ValueError).
