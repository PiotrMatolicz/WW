
def proba1(lista):
    del lista[0]
    for i in range(len(lista)):
        lista[i] *= 2
    lista.append('Gucio')


a = [10, 20, 30, 40]
print(a)
b = a
b.append(50)
print(a)

proba1(b)
print(a)
print()
