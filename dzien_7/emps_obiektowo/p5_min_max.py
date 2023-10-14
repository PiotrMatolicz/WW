from employee import *

emps = wczytaj_plik('emps.csv')

najbogatszy = None
najbiedniejszy = None
for emp in emps:
    if najbogatszy is None or emp.salary > najbogatszy.salary:
        najbogatszy = emp
    if najbiedniejszy is None or emp.salary < najbiedniejszy.salary:
        najbiedniejszy = emp

print('Najbogatszy:', najbogatszy)
print('Najbiedniejszy:', najbiedniejszy)
