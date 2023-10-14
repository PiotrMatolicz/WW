from osoba import Osoba

a = Osoba('Ala', 'Kowalska', 30)
b = Osoba('Ola', 'Malinowska', 16)

print(a)
print(b)
s = str(a)
print(s.upper())
print()

# W ten sposób można dostać się do atrybutów, które są w obiektach:
print('Imiona osób:', a.imie, b.imie)

# Atrybuty w obiektach mogą być zmieniane
# (dokładnie mówiąc mogą być, o ile klasa jest "mutowalna", tak jest domyślnie,
# ale np. str lub tuple są "niemutowalne" i w tych obiektach nie można niczego zmieniać)

a.imie = 'Alicja'
b.imie = 'Aleksandra'
print('Imiona osób po zmianie:', a.imie, b.imie)
print(a)
print(b)

# Jednym z sensownych sposobów użycia obiektów, jest umieszczenie ich w liście albo słowniku

osoby = [
    a,
    b,
    Osoba('Jan', 'Kowalski', 40),
    Osoba('Jadwiga', 'Hemel', 60),
    Osoba('Zeznon', 'Zezowaty', 33),
]

print('Wszystkie osoby:')
suma = 0
for o in osoby:
    print(o)
    suma += o.wiek

print('Średni wiek osób:', suma / len(osoby))
