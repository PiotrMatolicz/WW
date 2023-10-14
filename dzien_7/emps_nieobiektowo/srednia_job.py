job = input('Podaj nazwę stanowiska: ')
suma = 0
ile = 0
with open('emps.csv', mode='r', encoding='UTF-8') as plik:
    plik.readline()
    for linia in plik:
        pola = linia.split(';')
        if pola[3] == job:
            suma += int(pola[4])
            ile += 1

if ile > 0:
    srednia = suma / ile
    print(f'Średnia na stanowisku {job} wynosi {srednia:.2f}')
else:
    print('Nie znaleziono')
