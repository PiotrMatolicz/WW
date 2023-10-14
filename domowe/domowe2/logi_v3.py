# Uproszczenie: wystarczy użyć jednego słownika i dla każdego usera pamiętać tylko jedną liczbę – od razu sumę.
# Korzystając z niniejszego matematycznego przekształcenia, możemy dojść do wniosku,
# że wystarczy początki sesji wpisywać ze znakiem ujemnym, a wszystko ładnie się zsumuje.
# suma = (kon1 - pocz1) + (kon2 - pocz2)
# suma = (-pocz1 + kon1) + (-pocz2 + kon2)
# suma = -pocz1 + kon1 + -pocz2 + kon2

# Jeśli użyjemy default_dict, będzie jeszcze mniej pisania

from collections import defaultdict

suma_czasow = defaultdict(int)

with open('logs.txt', mode='r', encoding='utf-8') as plik:
    for line in plik:
        username, action, time_txt = line.strip().split(';')
        time = int(time_txt)
        if action == 'LOGIN':
            suma_czasow[username] -= time
        elif action == 'LOGOUT':
            suma_czasow[username] += time

for k, v in sorted(suma_czasow.items()):
    print(f'Suma sesji {k:8}: {v:6} s')
