class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.suma_godzin = 0

    def register_time(self, godziny):
        if godziny > 8:
            self.suma_godzin += 8
            self.suma_godzin += 2 * (godziny - 8)
        else:
            self.suma_godzin += godziny

    def pay_salary(self):
        try:
            return self.stawka * self.suma_godzin
        finally:
            self.suma_godzin = 0

