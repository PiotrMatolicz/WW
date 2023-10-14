# W tym programie obliczam statystyki dla wskzanego kraju.

wybrany_kraj = input('Podaj symbol wybranego kraju, np. POL: ').upper()

liczba = 0
suma_wag = 0
suma_wzrostu = 0
ile_najwyzszy = 0
kto_najwyzszy = None
ile_najnizszy = 1000
kto_najnizszy = None
ile_najciezszy = 0
kto_najciezszy = None
ile_najlzejszy = 1000
kto_najlzejszy = None

with open('zawodnicy.csv', mode='r', encoding='UTF-8') as plik:
    for linia in plik:
        imie, nazwisko, kraj, data_ur, wzrost_str, waga_str = linia.strip().split(';')
        if kraj == wybrany_kraj:
            wzrost = int(wzrost_str)
            waga = int(waga_str)
            liczba += 1
            suma_wag += waga
            suma_wzrostu += wzrost
            if wzrost > ile_najwyzszy:
                ile_najwyzszy = wzrost
                kto_najwyzszy = f'{imie} {nazwisko}'
            if wzrost < ile_najnizszy:
                ile_najnizszy = wzrost
                kto_najnizszy = f'{imie} {nazwisko}'
            if waga > ile_najciezszy:
                ile_najciezszy = waga
                kto_najciezszy = f'{imie} {nazwisko}'
            if waga < ile_najlzejszy:
                ile_najlzejszy = waga
                kto_najlzejszy = f'{imie} {nazwisko}'


print(f'Statystyki dla kraju {wybrany_kraj}:')
print(f'Liczba zawodników: {liczba}')
print(f'Suma wag         : {suma_wag}')
print(f'Średni wzrost    : {suma_wzrostu / liczba :.1f}')
print(f'Najwyższy zawodnik : {kto_najwyzszy}')
print(f'Najniższy zawodnik : {kto_najnizszy}')
print(f'Najcięższy zawodnik: {kto_najciezszy}')
print(f'Najlżejszy zawodnik: {kto_najlzejszy}')
