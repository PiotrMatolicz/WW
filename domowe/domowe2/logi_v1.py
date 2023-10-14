# Ta wersja na przykładzie dwóch userów ma wytłumaczyć, na czym będzie polegało zapisywanie danych poszczególnych userów w słowniku.
# W tej wersji używam dwóch par zmiennych, a za chwilę w wersji 2 będę miał zamiast tego dwa słowniki i w nich dane poszczególnych userów.

poczatek_sesji_user_1 = 0
suma_czasow_user_1 = 0

poczatek_sesji_user_2 = 0
suma_czasow_user_2 = 0


with open('logs.txt', mode='r', encoding='utf-8') as plik:
    for line in plik:
        fields = line.strip().split(';')
        username = fields[0]
        action = fields[1]
        time = int(fields[2])
        if username == 'Adam':
            if action == 'LOGIN':
                poczatek_sesji_user_1 = time
            elif action == 'LOGOUT':
                koniec_sesji = time
                czas_sesji = koniec_sesji - poczatek_sesji_user_1
                print(f'sesja Adama: {czas_sesji}')
                suma_czasow_user_1 += czas_sesji
        if username == 'Bartek':
            if action == 'LOGIN':
                poczatek_sesji_user_2 = time
            elif action == 'LOGOUT':
                koniec_sesji = time
                czas_sesji = koniec_sesji - poczatek_sesji_user_2
                print(f'sesja Bartka: {czas_sesji}')
                suma_czasow_user_2 += czas_sesji

print(f'Suma user-1: {suma_czasow_user_1}')
print(f'Suma user-2: {suma_czasow_user_2}')

