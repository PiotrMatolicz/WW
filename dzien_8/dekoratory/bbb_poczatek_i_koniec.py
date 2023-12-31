def dopisz_poczatek_i_koniec(funkcja):
    def zmieniona_funkcja():
        print('POCZATEK')
        funkcja()
        print('KONIEC')

    return zmieniona_funkcja


# Gdy mamy funkcję wyższego rzędu, czyli taką, które bierze funkcję i w wyniku zwraca inną (zmienioną) funkcję,
# to można jej używać jako dekoratora przed definicjami zwykłych funkcji.

@dopisz_poczatek_i_koniec
def powitaj():
    print('Witamy serdecznie')
# Dekorator robi coś takiego:
# powitaj = dopisz_poczatek_i_koniec(powitaj)


@dopisz_poczatek_i_koniec
def pozdrow():
    print('Na zdrowie!')

# Teraz pod oryginalnymi nazwami powitaj i pozdrów mamy zmienione funkcje.
powitaj()
powitaj()
print()

pozdrow()
