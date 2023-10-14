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

