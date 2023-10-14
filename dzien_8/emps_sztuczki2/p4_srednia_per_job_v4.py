from employee import *
from collections import defaultdict

emps = Employee.wczytaj_plik('emps.csv')

# W tej wersji łączymy zalety wersji 2 (defaultdict) i 3 (jeden słownik)
# Jako argument do defaultdict przekazuje się funkcję, która (bez argumentu) zwraca nowy element do wstawienia do słownika
slownik = defaultdict(lambda: [0, 0])

for emp in emps:
    slownik[emp.job_title][0] += 1
    slownik[emp.job_title][1] += emp.salary

for job, [ile, suma] in slownik.items():
    srednia = suma / ile
    print(f'{job:32} | {ile:2} | {srednia:8.2f}')
