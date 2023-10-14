from osoba import Osoba
from konto import Konto

ala = Osoba('Ala', 'Kowalska', 30)
konto1 = Konto(1, ala, 5000)
print(konto1)

# Dodaj do klasy Konto takie definicje, aby zadziałały operacje:
konto1.wplata(1000)
print(konto1) # saldo 6000

konto1.wyplata(700)
print(konto1) # saldo 5300
