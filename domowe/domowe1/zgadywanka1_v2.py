from random import randint

ZAKRES = 10

x = randint(1, ZAKRES)
y = randint(1, ZAKRES)
iloczyn = x * y
ile_prob = 1

propozycja = int(input(f'Ile to jest {x}×{y}? '))

while propozycja != iloczyn:
    ile_prob += 1
    propozycja = int(input('Niepoprawny wynik. Spróbuj jeszcze raz: '))

print(f'Brawo, poprawny wynik to {iloczyn}. Udało Ci się w {ile_prob} próbie.')
