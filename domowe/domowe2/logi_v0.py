# Tylko na rozgrzewkę obliczenie dla jednego wybranego usera.
# Operujemy tutaj na "zwykłych zmiennych", bez słowników.

poczatek_sesji = 0
suma_czasow = 0

with open('logs.txt', mode='r', encoding='utf-8') as plik:
    for line in plik:
        fields = line.strip().split(';')
        username = fields[0]
        action = fields[1]
        time = int(fields[2])
        if username == 'Adam':
            if action == 'LOGIN':
                poczatek_sesji = time
            elif action == 'LOGOUT':
                koniec_sesji = time
                czas_sesji = koniec_sesji - poczatek_sesji
                print(f'sesja user-1: {czas_sesji}')
                suma_czasow += czas_sesji

print('a kuku, plik jest zamknięty')
print(f'Suma user-1: {suma_czasow}')

