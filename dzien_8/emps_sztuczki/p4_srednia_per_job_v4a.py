from employee import *
from collections import defaultdict

emps = wczytaj_plik('emps.csv')

def nowy_element():
    return [0, 0]

# W tej wersji łączymy zalety wersji 2 (defaultdict) i 3 (jeden słownik)
slownik = defaultdict(nowy_element)

for emp in emps:
    slownik[emp.job_title][0] += 1
    slownik[emp.job_title][1] += emp.salary


for job, [ile, suma] in slownik.items():
    srednia = suma / ile
    print(f'{job:32} | {ile:2} | {srednia:8.2f}')
