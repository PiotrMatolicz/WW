from employee import *

emps = wczytaj_plik('emps.csv')

# W tym rozwiązaniu dane od razu doliczamy do słowników. Będą dwa słowniki liczące sumę pensji oraz liczbę pracowników.
# To jest klasyczny schemat "grupowania za pomocą słowników"

sumy = {}
ilosci = {}

for emp in emps:
    if emp.job_title in sumy:
        # to jest kolejny pracownik z tego stanowiska
        sumy[emp.job_title] += emp.salary
        ilosci[emp.job_title] += 1
    else:
        # to jest pierwszy pracownik na danym stanowisku
        sumy[emp.job_title] = emp.salary
        ilosci[emp.job_title] = 1

for job in sumy:
    suma = sumy[job]
    ile = ilosci[job]
    srednia = suma / ile
    print(f'{job:32} | {ile:2} | {srednia:8.2f}')
