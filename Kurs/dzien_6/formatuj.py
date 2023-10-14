def formatuj(*args, **kwargs):
    tekst = '\n'.join(args)
    for nazwa, wartosc in kwargs.items():
        tekst = tekst.replace('$'+nazwa, str(wartosc))
    return tekst


# w tym samym pliku umieszczamy testy pytest:
def test_formatuj_podstawianie():
    wynik = formatuj('Ala ma $zwierze i mieszka w $miasto',
                     zwierze='kota', miasto='Warszawie')
    assert wynik == 'Ala ma kota i mieszka w Warszawie'


def test_formatuj_samo_laczenie():
    wynik = formatuj(
        'Pierwsza linia',
        'Druga linia',
        'Trzecia linia',
    )
    assert wynik == 'Pierwsza linia\nDruga linia\nTrzecia linia'


def test_formatuj_laczenie_i_podstawianie():
    wynik = formatuj(
        'koszt $cena PLN',
        'kwota $cena brutto',
        cena=10,
    )
    assert wynik == 'koszt 10 PLN\nkwota 10 brutto'


def main():
    wynik = formatuj('Ala ma $zwierze i mieszka w $miasto',
                     zwierze='kota', miasto='Warszawie')
    print(wynik)

    wynik = formatuj(
        'koszt $cena PLN',
        'kwota $cena brutto',
        cena=10,
    )
    print(wynik)


if __name__ == '__main__':
    main()