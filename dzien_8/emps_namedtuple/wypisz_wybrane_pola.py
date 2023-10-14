from employee import *

# Nazwy kolumn da się odczytać z samego typu Employee:

print(Employee.__name__, ':', Employee._fields)

emps = wczytaj_plik('emps.csv')
for emp in emps:
    # do pól obiektu namedtuple można odwoływać się poprzez numery pozycji (jak dla elementu listy) oraz nazwy kolumn (jak do atrybutu obiektu)
    # emp[9] oznacza miasto
    print(emp.first_name, emp.last_name, emp.salary, emp[9])
