suma = 0
ile = 0
with open('emps.csv', mode='r', encoding='UTF-8') as plik:
    plik.readline()
    for linia in plik:
        pola = linia.split(';')
        suma += int(pola[4])
        ile += 1

srednia = suma / ile
print('Średnia wszystkich:', srednia)
