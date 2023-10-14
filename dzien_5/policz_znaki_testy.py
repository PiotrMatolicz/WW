from policz_znaki import policz_znaki

def test_policz_znaki_przypadek_podstawowy():
    wynik = policz_znaki('Ala ma <kota> i tyle.')
    assert wynik == 4

def test_policz_znaki_dwa_napisy():
    assert policz_znaki('Ala ma <kota> i <psa>.') == 7

def test_policz_znaki_inne_symbole():
    assert policz_znaki('ala ma [kota] a <kot> ma ale', '[', ']') == 4

def test_policz_znaki_zagniezdzenia():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18

def test_policz_znaki_koncowka():
    assert policz_znaki('a <a<a<aa>>a> xyz') == 10
