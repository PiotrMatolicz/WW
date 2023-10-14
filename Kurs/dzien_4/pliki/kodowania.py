with open('nowy_utf.txt', mode='w', encoding='UTF-8') as plik1:
    print('Ala ma kota 0123.', file=plik1)
    print('Żółte żonkile na łące pełnej gąsek.', file=plik1)
    print('Zażółć gęślą jaźń', file=plik1)


with open('nowy_win.txt', mode='w', encoding='cp1250') as plik2:
    print('Ala ma kota 0123.', file=plik2)
    print('Żółte żonkile na łące pełnej gąsek.', file=plik2)
    print('Zażółć gęślą jaźń', file=plik2)

print('Gotowe')
