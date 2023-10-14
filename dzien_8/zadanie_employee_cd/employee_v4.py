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
        self.kasa = 0

    def register_time(self, godziny):
        self.kasa += godziny * self.stawka
        if godziny > 8:
            self.kasa += (godziny - 8) * self.stawka

    def pay_salary(self):
        try:
            return self.kasa
        finally:
            self.kasa = 0


class PremiumEmployee(Employee):
    def give_bonus(self, bonus):
        self.kasa += bonus

# W tej wersji zakłądmay, że klasa Employee jest napisana w pewien konkretny sposób (chodzi o atrybut kasa)
# i wtedy implementacja PremiumEmployee może być bardzo krótka.
