from employee import Employee

emp = Employee(1, 'Jan', 'Kowalski', 'Księgowy', 15000, '2021-02-03', 'Księgowość', 'Jasna 14', '01-023', 'Warszawa', 'Polska')
print(emp)
print(f'{emp.last_name} pracuje w dziale {emp.department_name} w mieście {emp.city}')
