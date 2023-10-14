rozmiar = int(input('Podaj rozmiar choinki: '))

choinka = '\n'.join(' '*(rozmiar-i) + '*' * (2*i+1) for i in range(rozmiar))
print(choinka)
