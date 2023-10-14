def wiecej_niz(napis, liczba):
    """Funkcja zwraca zbiór tych znaków, które w napisie występują więcej razy, niż argument liczba."""
    slownik = {}
    for znak in napis:
        if znak in slownik:
            slownik[znak] += 1
        else:
            slownik[znak] = 1

    return {znak for znak in slownik if slownik[znak] > liczba}


wynik = wiecej_niz('ala ma kota a kot ma ale', 3)
print(wynik)
