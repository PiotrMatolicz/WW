from employee import Employee

# Aby wywołać metodę statyczną, piszemy NazwaKlasy.metoda(...)

emps = Employee.wczytaj_plik('emps.csv')
print(f'Wczytano {len(emps)} rekordów:')
for emp in emps:
    print(emp)
