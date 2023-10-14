import pandas

# emps = pandas.read_csv('emps.csv', sep=';')

emps = pandas.read_csv('emps.csv', sep=';', index_col='employee_id', parse_dates=['hire_date'])
print('Dane wczytane')
print(emps)

print('-'*80)
print('Średnia pensja:', emps.salary.mean())
print('Średnia pensja programistów:', emps[emps.job_title == 'Programmer'].salary.mean())
print('='*80)

# bierzemy rekord o ID = 100
king = emps.loc[100]
print(king)
print()
print(king.first_name, king.last_name, 'zarabia', king.salary)
print(king["first_name"], king["last_name"], 'zarabia', king["salary"])
