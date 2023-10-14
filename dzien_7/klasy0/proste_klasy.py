# definicja klasy
class Osoba:
    def czesc(self):
        print('Cześć!')

# koniec definicji klasy, gdy wracam na zerowy poziom wcięcia

# Dzięki temu, że zdefiniowałem klasę Osoba, mogę teraz stworzyć obiekt klasy Osoba
# i wpisać go do zmiennej:
a = Osoba()
print('W zmiennej a jest wartość typu:', type(a))
print('Gdy wypiszemy ten obiekt:', a)

# Dzięki temu, że w klasie zdefiniowaliśmy metodę czesc, możemy ją wywołać dla obiektu
a.czesc()
