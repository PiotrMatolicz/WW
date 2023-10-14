# Program wypisuje na ekran całą treść Pana Tadeusza numerując przy tym linie.

with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as plik:
    for nr, linia in enumerate(plik, 1):
        print(f'{nr:6}: {linia.strip()}')
