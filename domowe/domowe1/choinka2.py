rozmiar = int(input('Podaj rozmiar choinki: '))
for i in range(rozmiar):
    print(' ' * (rozmiar-i) + '*' * (2*i+1))
