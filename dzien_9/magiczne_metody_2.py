class MojaLiczba:
    def __init__(self, wartosc):
        self.wartosc = wartosc

    # definiując klasę możemy stworzyć nie tylko wymyślone przez nas metody o dowolnych nazwach,
    # ale możemy też przedefiniować metody przewidziane przez język Python,
    # których nazwy zaczynają się od __
    # - te metody wpływają na działanie obiektów naszej klasy w różnych sytuacjach:

    # str zwraca tekstową reprezentację obiektu, używaną np. przez print
    # To jest przeznaczone dla oczu człowieka :-)
    def __str__(self):
        return f'[{self.wartosc}]'

    # repr - tekstowy zapis obiektu, ale w takiej formie, że da się to wkleić do kodu i taki kod utworzy obiekt
    # To jest przeznaczone dla interpretera Pythona
    def __repr__(self):
        return f'MojaLiczba({repr(self.wartosc)})'

    # Definiując metody __add__, __sub__, __mul__, __truediv__ można określić działanie operatorów arytmetycznych
    def __add__(self, other):
        return MojaLiczba(self.wartosc + other.wartosc)

    def __sub__(self, other):
        return MojaLiczba(self.wartosc - other.wartosc)

    def __mul__(self, other):
        return MojaLiczba(self.wartosc * other.wartosc)

    # Metody __eq__, __lt__, __le__ ... pozwalają zdefiniować porównywanie
    def __eq__(self, other):
        return self.wartosc == other.wartosc

    def __lt__(self, other):
        return self.wartosc < other.wartosc

    def __le__(self, other):
        return self.wartosc <= other.wartosc


a = MojaLiczba(3)
b = MojaLiczba(5)

print('str:', a, b)
print('repr:', repr(a), repr(b))
print('a + b:', a+b)
wynik = a+b
print('wynik jest typu', type(wynik))

print('b - a:', b-a)
print('a * b:', a*b)
print()

print('a == b:', a == b)
print('a != b:', a != b)
print('a < b:', a < b)
print('a <= b:', a <= b)
print('a > b:', a > b)
print('a >= b:', a >= b)

