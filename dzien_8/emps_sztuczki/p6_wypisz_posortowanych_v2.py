from employee import *

emps = wczytaj_plik('emps.csv')
print(f'Wczytano {len(emps)} rekordów:')

for emp in sorted(emps, key=lambda emp: emp.salary, reverse=True):
    print(emp)
