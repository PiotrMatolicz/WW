from typing import List, NoReturn, Tuple, Sequence, Any


class Employee:
    nazwy_kolumn = ('employee_id', 'first_name', 'last_name', 'job_title', 'salary', 'hire_date',
                 'department_name', 'address', 'postal_code', 'city', 'country')

    SEP = ';'

    def __init__(self, employee_id, first_name, last_name, job_title, salary, hire_date,
                 department_name, address, postal_code, city, country):
        self.employee_id = int(employee_id)
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.salary = int(salary)
        self.hire_date = hire_date
        self.department_name = department_name
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.country = country

    def __str__(self):
        return f'Pracownik nr {self.employee_id}: {self.first_name} {self.last_name} ({self.job_title}), pensja {self.salary}'

    @property
    def wszystkie_pola(self):
        # pobranie wartości wszystkich atrybutów obiektu w takiej kolejności, jak wpisane w init
        return self.__dict__.values()
        # gdybyśmy mieli wątpliwości co do olejności kolumn, to można też tak:
        # return [self.__dict__[kolumna] for kolumna in Employee.nazwy_kolumn]

    def zmien_pensje(self, zmiana:int) -> NoReturn:
        self.salary += zmiana

    @staticmethod
    def wczytaj_plik(sciezka:str) -> List['Employee']:
        lista = []
        with open(sciezka, mode='r', encoding='utf-8') as plik:
            plik.readline()
            for linia in plik:
                t = linia.strip().split(Employee.SEP)
                emp = Employee(*t)
                lista.append(emp)
        return lista

    @staticmethod
    def zapisz_plik(emps:List['Employee'], sciezka:str) -> NoReturn:
        with open(sciezka, mode='w', encoding='utf-8') as plik:
            print(*Employee.nazwy_kolumn, sep=Employee.SEP, file=plik)
            for emp in emps:
                print(*emp.wszystkie_pola, sep=Employee.SEP, file=plik)
