from employee import *

emps = wczytaj_plik('emps.csv')
print(f'Wczytano {len(emps)} rekordów:')
for emp in emps:
    print(emp)
