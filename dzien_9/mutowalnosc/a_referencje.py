
class Konto:
    def __init__(self, wlasciciel, saldo=0):
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def __str__(self):
        return f'Konto {self.wlasciciel}, saldo: {self.saldo}'

    def __repr__(self):
        return f'Konto({repr(self.wlasciciel)}, {repr(self.saldo)})'

    def wplata(self, kwota):
        self.saldo += kwota

# Zmienna w Pythonie jest referencją do obiektu.
# Mówiąc technicznie: w zmiennej zapisany jest adres, pod którym w pamięci znajduje się obiekt.

a = Konto('Ala', 1000)
b = Konto('Ola', 2000)
c = b

print('a:', a)
print('b:', b)
print('c:', c)
print()

b.wplata(300)
print('a:', a)
print('b:', b)
print('c:', c)
print()

b = a
print('a:', a)
print('b:', b)
print('c:', c)

# domyślnie operacja przypisania a = b nie kopiuje obiektu
# Python posiada gotowe operacje do kopiowania obiektów

from copy import copy, deepcopy

kopia = copy(a)
print('k:', kopia)
print()

a.wplata(123)

print('a:', a)
print('b:', b)
print('c:', c)
print('k:', kopia)
print()

lista1 = [a, b, c]
lista2 = lista1
lista3 = copy(lista1) # płytka kopia - oddzielna lista, ale w niej referencje do tych samych obiektów
lista4 = deepcopy(lista1) # głęboka kopia - róœnież zawartość listy (obiekty) jest kopiowana

print('lista1:', lista1)
print('lista2:', lista2)
print('lista3:', lista3)
print('lista4:', lista4)
print()

lista1.append(Konto('Ela'))
a.wplata(70)
lista1[0].wplata(7)

print('lista1:', lista1)
print('lista2:', lista2)
print('lista3:', lista3)
print('lista4:', lista4)
