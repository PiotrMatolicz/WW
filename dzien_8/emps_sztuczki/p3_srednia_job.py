from employee import *

emps = wczytaj_plik('emps.csv')
job = input('Podaj nazwę stanowiska: ')

suma = 0
ile = 0
for emp in emps:
    if emp.job_title == job:
        suma += emp.salary
        ile += 1

if ile > 0:
    srednia = suma / ile
    print(f'Średnia na stanowisku {job} wynosi {srednia:.2f}')
else:
    print('Nie znaleziono')
