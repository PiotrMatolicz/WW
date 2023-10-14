# Dla każdego pracownika wypiszemy jego imię, nazwisko, stanowisko i pensję.

with open('emps.csv', mode='r', encoding='UTF-8') as plik:
    for linia in plik:
        pola = linia.split(';')
        print(pola[1], pola[2], '(stanowisko', pola[3], ') zarabia', pola[4])

'''Zadania:
- oblicz średnią pensję wszystkich pracowników

- użytkownik wpisuje rodzaj stanowiska (np. Programmer), 
  a program oblicza ile jest takich osób oraz średnią pensję na tym stanowisku
'''