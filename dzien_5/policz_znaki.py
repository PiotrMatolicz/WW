def policz_znaki(napis, zp='<', zk='>'):
    poziom = 0
    liczba_znakow = 0
    for litera in napis:
        if litera == '<':
            poziom += 1
        elif litera == '>':
            poziom -= 1
        else:
            liczba_znakow += poziom
    return liczba_znakow


# Tak napisany if powoduje, że kod umieszczony w tym ifie wykona się
# tylko wtedy, gdy ten plik jest uruchamiany bezpośrednio jako program Pythona
# a nie wykona się, gdy ten plik jest importowany jako moduł przez inny program.
if __name__ == '__main__':
    print(policz_znaki('ala ma <kota> a kot ma ale'))    # 4
    print(policz_znaki('ala ma <kota> a <kot> ma ale'))  # 7
    print(policz_znaki('ala ma [kota] a <kot> ma ale', '[', ']'))  # 4
    print(policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']')) # 18
    print(policz_znaki('a <a<a<aa>>a> xyz')) # 10

