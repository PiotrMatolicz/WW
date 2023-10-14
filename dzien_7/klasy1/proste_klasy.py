# definicja klasy
class Osoba:
    # Aby opisać, jakie atrybuty mają być zapisane w obiekcie po jego utworzeniu,
    # należy zdefiniować metodę init:
    def __init__(self, imie, nazwisko):
        # wartość imie przekazaną w parametrze zapisujemy jako atrybut wewnątrz obiektu
        self.imie = imie
        self.nazwisko = nazwisko

    def czesc(self):
        print(f'Cześć! Jestem {self.imie}.')

# koniec definicji klasy, gdy wracam na zerowy poziom wcięcia

# Dzięki temu, że zdefiniowałem klasę Osoba, mogę teraz stworzyć obiekt klasy Osoba
# i wpisać go do zmiennej:
a = Osoba('Ala', 'Kowalska')
print('W zmiennej a jest wartość typu:', type(a))
print('Gdy wypiszemy ten obiekt:', a)

# Można tworzyć wiele obiektów tej samej klasy
b = Osoba(imie='Bartek', nazwisko='Malinowski')
print('Gdy wypiszemy obiekt b  :', b)
print()

# Dzięki temu, że w klasie zdefiniowaliśmy metodę czesc, możemy ją wywołać dla obiektu
a.czesc()
b.czesc()
