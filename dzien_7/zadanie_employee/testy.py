from employee_v4 import Employee

def test_employee_jedna_praca():
    employee = Employee('Jan', 'Nowak', 100)
    employee.register_time(5)
    salary = employee.pay_salary()
    assert salary == 500

def test_employee_kilka_prac():
    employee = Employee('Jan', 'Nowak', 100)
    employee.register_time(4)
    employee.register_time(6)
    employee.register_time(8)
    salary = employee.pay_salary()
    assert salary == 1800

def test_employee_reset():
    employee = Employee('Jan', 'Nowak', 100)
    employee.register_time(12)
    employee.register_time(3)
    # wykonujemy jedno pay_salary, aby pobrać wypłatę, ale jej wartości tu nie spawdzamy
    employee.pay_salary()
    # wykonujemy drugie pay_salary i srpawdzamy, czy teraz wynik jest równy zero
    salary = employee.pay_salary()
    assert salary == 0


def test_employee_nadgodziny():
    employee = Employee('Jan', 'Nowak', 100)
    employee.register_time(10)
    employee.register_time(10)
    employee.register_time(3)
    # 8 * 100 + 2 * 200 + 8 * 100 + 2 * 200 + 3 * 100 = 2700
    salary = employee.pay_salary()
    assert salary == 2700
