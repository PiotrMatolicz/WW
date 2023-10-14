class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        # można tworzyć również atrybuty, które nie występują jako parametry init
        self.suma_godzin = 0

    def register_time(self, godziny):
        self.suma_godzin += godziny

    def pay_salary(self):
        wynik = self.stawka * self.suma_godzin
        self.suma_godzin = 0
        return wynik
