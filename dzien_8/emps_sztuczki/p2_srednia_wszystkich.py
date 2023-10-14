from employee import *

# W tej wersji nie otwieramy już pliku za pomocą with open, nie czytamy linii itd.,
# tylko korzystamy z gotowej operacji
emps = wczytaj_plik('emps.csv')

# Teraz w zmiennej emps mamy listę obiektów klasy Employee
print(f'Wczytano {len(emps)} rekordów.')

suma = 0
for emp in emps:
    suma += emp.salary

srednia = suma / len(emps)
print('Średnia:', srednia)
