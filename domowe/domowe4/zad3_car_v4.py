class ElectricCar:
    """
    Zaimplementuj klasę ElectricCar odwzorowującą zachowanie
    samochodu elektrycznego. Klasa powinna umożliwiać pokonanie
    zadanego dystansu, który nie może przekroczyć maksymalnego
    zasięgu zdefiniowanego dla samochodu. Samochód powinien
    mieć także możliwość naładowania baterii.
    >>> car = ElectricCar(100)
    >>> car.drive(70)
    70
    >>> car.drive(50)
    30
    >>> car.drive(50)
    0
    >>> car.charge()
    >>> car.drive(50)
    50
    """

    def __init__(self, zasieg):
        self.max_zasieg = zasieg
        self.biezacy_zasieg = zasieg

    def drive(self, dystans):
        if dystans > self.biezacy_zasieg:
            dystans = self.biezacy_zasieg
        self.biezacy_zasieg -= dystans
        return dystans

    def charge(self):
        self.biezacy_zasieg = self.max_zasieg


#### Tutaj kilka testów pytest ####

def test_drive1():
    car = ElectricCar(100)
    km = car.drive(70)
    assert km == 70

def test_drive_do_konca():
    car = ElectricCar(100)
    km = car.drive(70)
    km = car.drive(50)
    assert km == 30

def test_wyladowanie_do_zera():
    car = ElectricCar(100)
    km = car.drive(150)
    km = car.drive(50)
    assert km == 0

def test_charge1():
    car = ElectricCar(200)
    car.drive(150)
    car.drive(100)
    car.charge()
    km = car.drive(150)
    assert km == 150

def test_charge2():
    car = ElectricCar(500)
    car.drive(300)
    car.charge()
    km = car.drive(600)
    assert km == 500

