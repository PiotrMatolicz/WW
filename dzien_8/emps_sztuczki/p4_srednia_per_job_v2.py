from employee import *
from collections import defaultdict

emps = wczytaj_plik('emps.csv')

# W tej wersji stosujemy defaultdict, dzięki czemu nie musimy przejmować się wstawianiem początkowych danych
# W razie braku danych, defaultdict automatycznie wstawi wartość 0

sumy = defaultdict(float)
ilosci = defaultdict(int)

for emp in emps:
    sumy[emp.job_title] += emp.salary
    ilosci[emp.job_title] += 1

for job in sumy:
    suma = sumy[job]
    ile = ilosci[job]
    srednia = suma / ile
    print(f'{job:32} | {ile:2} | {srednia:8.2f}')
