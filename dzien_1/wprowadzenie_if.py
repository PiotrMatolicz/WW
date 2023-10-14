liczba = int(input('Podaj liczbe: '))

print('Przed ifem')

if liczba == 10:
    print('Wpisales liczbe 10, swietnie!')
    print('Nadal jestem w ifie...')
elif liczba == 20:
    print('O, a teraz 20. Niezle!')
elif liczba % 2 == 0:
    print('Liczba jest parzysta')
else:
    print('Warunki nie zostaly spelnione')

print('Za ifem')
