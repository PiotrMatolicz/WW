# W tym programie obliczam statystyki "per kraj" za pomocą słowników (tylko liczba i średni wzrost).

ile_per_kraj = {}
suma_wzrostu_per_kraj = {}

with open('zawodnicy.csv', mode='r', encoding='UTF-8') as plik:
    for linia in plik:
        imie, nazwisko, kraj, data_ur, wzrost_str, waga_str = linia.strip().split(';')
        wzrost = int(wzrost_str)
        ile_per_kraj[kraj] = ile_per_kraj.get(kraj, 0) + 1
        suma_wzrostu_per_kraj[kraj] = suma_wzrostu_per_kraj.get(kraj, 0) + wzrost

for kraj in ile_per_kraj:
    ile = ile_per_kraj[kraj]
    suma = suma_wzrostu_per_kraj[kraj]
    srednia = suma / ile
    print(f'{kraj}: {ile} zawodników o średnim wzroście {srednia:.1f} cm')
