from osoba import Osoba
from konto import Konto

ala = Osoba('Ala', 'Kowalska', 30)
konto1 = Konto(1, ala, 5000)
konto2 = Konto(2, ala)
print(konto1)

konto1.wplata(1000)
print(konto1)

konto1.wyplata(700)
print(konto1)

# W tej wersji metody wplata i wyplata sprawdzają, czy przekazane do ich argumenty są sensowne, np. czy nie są ujemne
# konto1.wplata(-200)
print(konto1)


# Gdy atrybutry w klasie zdefiniujemy w stylu _nazwa, to dajemy znać,
# że programiści "nie powinni" odwoływać się do tego atrybutu, tylko traktować jak atrybut prywatny.
# Ale jeśli programista mimo wszystko odwoła się do takiego atrybutu, to kod zadziała.
konto1._saldo = -3333
print(konto1)

konto1._saldo = 'zhackowałem twoje konto'
print(konto1)


