class Konto:
    def __init__(self, numer, wlasciciel, saldo=0):
        self._numer = numer
        self._wlasciciel = wlasciciel
        self._saldo = saldo

    def __str__(self):
        return f'Konto nr {self._numer}, wł {self._wlasciciel}, saldo {self._saldo}'

    def wplata(self, kwota):
        if kwota < 0:
            raise ValueError(f'Kwota wpłaty jest ujemna: {kwota}')
        self._saldo += kwota

    def wyplata(self, kwota):
        if kwota < 0:
            raise ValueError(f'Kwota wypłaty jest ujemna: {kwota}')
        if kwota > self._saldo:
            raise ValueError(f'Masz za mało pieniędzy na koncie')
        self._saldo -= kwota