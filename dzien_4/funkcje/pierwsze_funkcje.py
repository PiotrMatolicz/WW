# Napisz funkcję powtorz , która przyjmuje dwa parametry: napis oraz liczbę powtórzeń
# i wypisuje na ekran podany napis tyle raze, ile wynosi drugi argument.

def powtorz(napis, liczba):
    for _ in range(liczba):
        print(napis)


def powtorz_v2(napis, liczba):
    print((napis+'\n') * liczba, end='')


powtorz('Ala ma kota', 5)
powtorz('Ola nie ma psa', 3)

powtorz_v2('Ela ma kota i psa', 4)
