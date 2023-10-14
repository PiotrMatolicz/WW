class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def __str__(self):
        return f'{self.imie} {self.nazwisko} ({self.wiek} l.)'

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

    def pelnoletnia(self):
        return self.wiek >= 18


class Student(Osoba):
    def __init__(self, imie, nazwisko, wiek, kierunek, rok):
        super().__init__(imie, nazwisko, wiek)
        self.kierunek = kierunek
        self.rok = rok
        self.oceny = []

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def srednia_ocen(self):
        return sum(self.oceny) / len(self.oceny)

    def przedstaw_sie(self):
        print(f'Hejka, tu {self.imie} {self.nazwisko}, studiuje kierunek {self.kierunek}!')

    def __str__(self):
        return super().__str__() + f', student {self.rok} roku kierunku {self.kierunek}'
