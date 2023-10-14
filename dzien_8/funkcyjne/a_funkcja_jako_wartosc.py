def powitaj():
    print('Witaj serdecznie!')

def pozegnaj():
    print('Do widzenia.')

print('Początek programu')
powitaj()

# Funkcję można wpisać do zmiennej
f = powitaj
# Teraz w zmiennej f mamy funkcję i możemy ją wywołać
f()
f = pozegnaj
f()
print()

# Funkcja może być elementem kolekcji (lista, słownik...)

funkcje = [powitaj, lambda: print('Mówię coś'), pozegnaj]
print(funkcje)
for funkcja in funkcje:
    funkcja()
print("=" * 20)

# Teraz funkcje, które biorą dwa argumenty i zwracają wynik, jak działąnia matematyczne.
def dodaj(a, b):
    return a+b

def pomnoz(x, y):
    return x*y

def liczba_z_cyfr(a, b):
    return 10*a + b


arg1 = 5
arg2 = 3
for funkcja in dodaj, pomnoz, liczba_z_cyfr:
    wynik = funkcja(arg1, arg2)
    print(f'Funkcja {funkcja.__name__} dla argumentów {arg1} i {arg2} dała wynik {wynik}')

