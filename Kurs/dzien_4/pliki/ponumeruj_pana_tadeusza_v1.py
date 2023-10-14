# Program wypisuje na ekran całą treść Pana Tadeusza numerując przy tym linie.

with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as plik:
    nr = 0
    for linia in plik:
        nr += 1
        print(nr, linia, end='')
