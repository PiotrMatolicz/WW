dane = input('Podaj dane: ')  # input zawsze odda str

print(dane)
print(type(dane))

"""
Konwersja typów danych
Mamy do dyspozycji szereg funkcji, które konwertują jeden typ danych na drugi:
- int(argument)
- float(argument)
- str(argument)
- bool(argument)
"""
dane_int = int(dane)
print(dane_int)
print(type(dane_int))

dane_float = float(dane)
print(dane_float)
print(type(dane_float))
