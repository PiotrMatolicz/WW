class MojaLiczba:
    '''
    Obiekt tej klasy pamięta w sobie liczbę,
    gdy użyjemy str, to wypisuje tę liczbę w [nawiasach],
    a na obiektach tej klasy można wykonywać operacje + - * < ...
    '''
    def __init__(self, wartosc):
        self._wartosc = wartosc

    def __str__(self):
        return f'[{self._wartosc}]'

    def __repr__(self):
        return f'MojaLiczba({self._wartosc})'

    def __add__(self, other):
        return MojaLiczba(self._wartosc + other._wartosc)


def main():
    a = MojaLiczba(5)
    b = MojaLiczba(7)
    print(a)
    print(b)

    print('str:', str(a), str(b))
    print('repr:', repr(a), repr(b))
    c = a + b
    print(c, 'typu', type(c))


if __name__ == '__main__':
    main()
