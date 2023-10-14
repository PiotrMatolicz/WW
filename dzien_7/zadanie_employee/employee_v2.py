class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        # można tworzyć również atrybuty, które nie występują jako parametry init
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

