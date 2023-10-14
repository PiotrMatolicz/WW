rozmiar = int(input('Podaj rozmiar choinki: '))
for i in range(rozmiar):
    for j in range(rozmiar - i):
        print(' ', end='')
    for j in range(2*i + 1):
        print('*', end='')
    print()
