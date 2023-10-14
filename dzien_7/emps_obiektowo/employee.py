from typing import List, NoReturn

class Employee:
    def __init__(self, employee_id, first_name, last_name, job_title, salary, hire_date,
                 department_name, address, postal_code, city, country):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.salary = salary
        self.hire_date = hire_date
        self.department_name = department_name
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.country = country


    def __str__(self):
        return f'Pracownik nr {self.employee_id}: {self.first_name} {self.last_name} ({self.job_title}), pensja {self.salary}'


# Funkcja odczytująca dane pracowników z pliku i zwracająca listę obiektów Employee
def wczytaj_plik(sciezka:str) -> List[Employee]:
    lista = []
    with open(sciezka, mode='r', encoding='utf-8') as plik:
        plik.readline()
        for linia in plik:
            t = linia.strip().split(';')
            emp = Employee(int(t[0]), t[1], t[2], t[3], int(t[4]), t[5], t[6], t[7], t[8], t[9], t[10])
            lista.append(emp)
    return lista


def zapisz_plik(emps:List[Employee], sciezka:str) -> NoReturn:
    with open(sciezka, mode='w', encoding='utf-8') as plik:
        plik.write('employee_id;first_name;last_name;job_title;salary;hire_date;department_name;address;postal_code;city;country\n')
        for emp in emps:
            print(emp.employee_id, emp.first_name, emp.last_name, emp.job_title, emp.salary,
                  emp.hire_date, emp.department_name, emp.address, emp.postal_code, emp.city, emp.country,
                  sep=';', file=plik)
