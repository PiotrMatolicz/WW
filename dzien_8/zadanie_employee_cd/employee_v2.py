'''
Zaimplementuj klasę PremiumEmployee, która będzie klasą
pochodną Employee. Klasa ta powinna umożliwiać dodatkowo
przyznawanie bonusów pracownikowi.
>>> employee = PremiumEmployee('Jan', 'Nowak', 100.0)
>>> employee.register_time(5)
>>> employee.give_bonus(1000.0)
>>> employee.pay_salary()
1500.0
'''

class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.suma_godzin = 0
        self.suma_nadgodzin = 0

    def register_time(self, godziny):
        if godziny > 8:
            self.suma_godzin += 8
            self.suma_nadgodzin += godziny - 8
        else:
            self.suma_godzin += godziny

    def pay_salary(self):
        try:
            return self.stawka * self.suma_godzin + self.stawka*2 * self.suma_nadgodzin
        finally:
            self.suma_godzin = 0
            self.suma_nadgodzin = 0


class PremiumEmployee(Employee):
    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        try:
            return super().pay_salary() + self.bonus
        finally:
            self.bonus = 0

# W tej wersji klasa PremiumEmployee jest napisana w taki sposób, który nie zakłada żadnych szczegółów implementacji
# w klasie Employee. Wystarczy, aby klasa Employee działała zgodnie z opisem z poprzedniego zadania,
# a tak napisana PremiumEmployee będzie poprawna.
# Nadpisujemy init oraz pay_salary w taki sposób, że kporzystamy z wersji napisanych już w nadklasie (super()).