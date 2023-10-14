
def dodaj1(lista, *nowe_elementy):
    lista.extend(nowe_elementy)


def dodaj2(lista, nowe_elementy):
    # przy takim zapisie nowy obiekt jest zapisywany na zmienną lista
    lista = lista + nowe_elementy
    print('lokalnie:', lista)


lista = ['Ala', 'Ola']
print(lista)
dodaj1(lista, 'Ula', 'Jula')
print(lista)

lista = lista + ['jabłko', 'pomarańcza']
print(lista)

dodaj2(lista, ['kapusta', 'kalafior'])
print(lista)
