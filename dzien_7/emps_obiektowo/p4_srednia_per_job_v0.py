from employee import *

emps = wczytaj_plik('emps.csv')

# etap 1: ustalamy, jakie są nazwy jobów bez powtórzeń
jobs = {emp.job_title for emp in emps}

# etap 2: dla każdego joba przeglądamy wszystkich pracowników i wybieramy tych, którzy mają określony job
# (dla każdego joba powtarzamy algorytm z programu p3)
for job in jobs:   # for job in sorted(jobs):
    suma = 0
    ile = 0
    for emp in emps:
        if emp.job_title == job:
            suma += emp.salary
            ile += 1
    srednia = suma / ile
    print(f'{job:32} | {ile:2} | {srednia:8.2f}')


# To rozwiązanie nie ma optymalnej wydajności. Dla każdgo joba przeglądamy całe dane od nowa.
# W następnych wersjach przeglądamy dane tylko raz.