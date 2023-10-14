from employee import *

emps = wczytaj_plik('emps.csv')

# W tej wersji dane wstawiamy do pojedynczego słownika, w którym wartościami są dwuelementowe listy
# job: [ilosc, suma]
slownik = {}

for emp in emps:
    if emp.job_title in slownik:
        # to jest kolejny pracownik z tego stanowiska
        slownik[emp.job_title][0] += 1
        slownik[emp.job_title][1] += emp.salary
    else:
        # to jest pierwszy pracownik na danym stanowisku
        slownik[emp.job_title] = [1, emp.salary]

# dwupoziomowe rozpakowywanie
for job, [ile, suma] in slownik.items():
    srednia = suma / ile
    print(f'{job:32} | {ile:2} | {srednia:8.2f}')
