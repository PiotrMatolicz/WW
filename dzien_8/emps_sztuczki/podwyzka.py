from employee import *

emps = wczytaj_plik('emps.csv')
job = input('Podaj nazwę stanowiska: ')
podwyzka = int(input('Podaj kwotę podwyżki: '))

for emp in emps:
    if emp.job_title == job:
        emp.zmien_pensje(podwyzka)

zapisz_plik(emps, 'zmienione.csv')
