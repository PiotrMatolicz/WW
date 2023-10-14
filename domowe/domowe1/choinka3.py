SPACJA = '-'
ZNAK = '@'

rozmiar = int(input('Podaj rozmiar choinki: '))
for i in range(rozmiar):
    spacje = SPACJA * (rozmiar - i)
    znaki = ZNAK * (2 * i + 1)
    print(spacje + znaki + spacje)
