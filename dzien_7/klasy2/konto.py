class Konto:
    def __init__(self, numer, wlasciciel, saldo):
        self.numer = numer
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def __str__(self):
        return f'Konto nr {self.numer}, wł {self.wlasciciel}, saldo {self.saldo}'

    def wplata(self, kwota):
        self.saldo += kwota

    def wyplata(self, kwota):
        self.saldo -= kwota