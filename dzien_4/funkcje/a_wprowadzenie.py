print('Początek programu')

# Funkcja to jest fragment programu, któremu nadajemy jakąś nazwę.
# Instrukcja def zapamiętuje funkcję, ale jej nie uruchamia.
def pierwsza_funkcja():
    print('Początek funkcji')
    print('pierwsza_funkcja działa, lalalalala')
    print('Koniec funkcji')

print('Pierwsza funkcja jest zdefiniowana:', pierwsza_funkcja)
print()

# Dopiero wywołanie (call, invoke) funkcji powoduje, że wykona się jej treść
print('Teraz uruchomię tę funkcję dwa razy')
pierwsza_funkcja()
pierwsza_funkcja()
print()

# Funkcje mogą mieć zadeklarowane parametry:
def powitaj_kursanta(imie, nazwa_kursu, czas_trwania):
    print(f'{imie}, witaj na kursie "{nazwa_kursu}"')
    print(f'Kurs potrwa {czas_trwania} dni')

# W momencie wywoływania tej funkcji, należy przekazać do niej wartości parametrów (czyli "argumenty"):
powitaj_kursanta('Andrzej', 'Programowanie w języku Java', 10)
powitaj_kursanta('Alicja', 'Analiza danych w Pythonie', 12)
print()

# Funkcje mogą zwracać wynik za pomocą return
# weekday zwraca nr dnia tygodnia licząc od poniedziałku = 0
# my w naszej funkcji "poprawiamy to" dodając jedynkę i nasza funkcja zwraca numery dni tygodnia z zakresu 1-7
def dzisiejszy_dzien():
    from datetime import datetime
    return datetime.now().weekday() + 1


def biezaca_sekunda():
    from datetime import datetime
    return datetime.now().second


def kwadrat(liczba):
    return liczba * liczba


# Gdy wywołamy taką funkcję, to możemy odczytać jej wynik i np. zapisać do zmiennej:
dzien = dzisiejszy_dzien()
sekunda = biezaca_sekunda()
print(f'Dzisiaj mamy dzień nr {dzien}, a teraz jest sekunda nr {sekunda}')

wynik = kwadrat(5)
print('Wynik podnoszenia do kwadratu:', wynik)
print('Inny kwadrat', kwadrat(7))

# Funkcję, która zwraca wynik, można też wywołać nie odbierając tego wyniku - wtedy on nigdzie się nie wypisze
kwadrat(9) # liczba 81 nigdzie się nie wypisuje
# !!! RETURN TO NIE TO SAMO CO PRINT !!!

# Z kolei jeśli spróbujemy odebrać wynik z funkcji, która nie robi return, to dostaniemy wartość None
print()
wynik = pierwsza_funkcja()
print('Wynik pierwszej funkcji:', wynik)

print()
print('Koniec programu')
