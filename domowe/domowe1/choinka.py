wysokosc = int(input('Podaj wysokość choinki: '))

for i in range(wysokosc):
    print(' ' * (wysokosc - i) + '*' * (2*i + 1))
