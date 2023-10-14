# Gdy definiujemy funkcję, ale w jej treści zamiast return użyjemy yield,
# to funkcja zwraca w wyniku "generator", czyli obiekt, który dostarcza kolejnej wartości dopiero wtedy, gdy jest o to proszony.
def abc():
    yield 'Ala'
    yield 'Basia'
    print('Jestem w funkcji abc między Basią a Celiną')
    yield 'Celina'


print(abc)
generator = abc()
print(generator)
# generator zwróci wartości (które w nim są zwracane za pomocą yield) wtedy, gdy wywołamy funkcję next
pierwszy_wynik = next(generator)
print(pierwszy_wynik)
print('Zaraz zapytam o Basię...')
nastepny_wynik = next(generator)
print(nastepny_wynik)
print('Zaraz zapytam o Celinę...')
nastepny_wynik = next(generator)
print(nastepny_wynik)
# Gdy nie ma już elementów, to wtedy pojawia się wyjątek StopIteration
try:
    nastepny_wynik = next(generator)
    print(nastepny_wynik)
except StopIteration:
    print('To już koniec')

print((40*'-'))

# Najczęściej z generatorów i iteratorów korzysta się tak, że umieszcza się po prawej stronie wyrażenia for
# i wtedy pętla for wykona się dla każdego elementu zwracanego przez ten generator.
for imie in abc():
    print('Kolejna osoba to', imie)
print((40*'-'))

# Najczęściej yield umieszcza się w pętli, a nie pisze jeden pod drugim.
# Ten generator wygeneruje określoną liczbę liczb nieparzystych.
def nieparzyste(ile):
    x = 1
    for i in range(ile):
        yield x
        x += 2

for n in nieparzyste(10):
    print(n, end=', ')
print()

print(sum(nieparzyste(7)))


def nasz_range(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i += step

print(list(nasz_range(100, 150, 5)))
