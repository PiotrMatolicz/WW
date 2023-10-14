from employee import *

emps = wczytaj_plik('emps.csv')
print(f'Wczytano {len(emps)} rekordów:')

emps.sort(key=lambda emp: emp.salary, reverse=True)

for emp in emps:
    print(emp)
