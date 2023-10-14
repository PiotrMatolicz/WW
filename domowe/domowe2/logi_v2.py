# Ta wersja liczy już czasy dla wszystkich userów, używając dla każdego "algorytmu" podanego we wcześniejszych wersjach:
# - gdy widzimy początek sesji (LOGIN), zapisujemy czas początku sesji w słowniku poczatek_sesji
# - gdy widzimy koniec  sesji (LOGOUT), to od bieżącego czasu odejmujemy zapamiętany wcześniej czas początku i mamy obliczony czas sesji. Dodajemy go do sumy.

poczatek_sesji = {}
suma_czasow = {}


with open('logs.txt', mode='r', encoding='utf-8') as plik:
    for line in plik:
        fields = line.strip().split(';')
        username = fields[0]
        action = fields[1]
        time = int(fields[2])
        if action == 'LOGIN':
            poczatek_sesji[username] = time
        elif action == 'LOGOUT':
            czas_sesji = time - poczatek_sesji[username]
            print(f'koniec sesji {username:8}, czas sesji: {czas_sesji:5}')
            if username not in suma_czasow:
                suma_czasow[username] = 0
            suma_czasow[username] += czas_sesji

for k, v in suma_czasow.items():
    print(f'Suma sesji {k:8}: {v:6} s')


