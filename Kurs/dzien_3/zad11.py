"""
Napisz program zliczający liczbę unikalnych liczb wprowadzonych
przez użytkownika. Sprawdź jak dużo z tych liczb jest liczbami
parzystymi w zakresie 0-100 - w tym celu skorzystaj z operatora iloczynu.
Zakładamy, że użytkownik wprowadza kolejne liczby (tyle, ile chce), a na końcu wciska enter
"""

liczby = set()

while True:
    dane = input(':')
    if not dane: break
    liczby.add(int(dane))

print('Wprowadzone liczby:', liczby)

# Tworzymy zbiór liczb parzystych z zakresu od 0 do 100 włącznie,
# aby wykorzystać do części wspólnej...
# sposób 1: zwykła pętla
# parzyste = set()
# for x in range(0, 101):
#     if x % 2 == 0:
#         parzyste.add(x)

# sposób 2: wyrażenie zbiorotwórcze ("set comprehension"):
# parzyste = {x for x in range(0, 101) if x % 2 == 0}

# sposób 3: range z krokiem
parzyste = set(range(0, 101, 2))

print('Wszystkie parzyste:', parzyste)

wybrane_parzyste = liczby & parzyste
print('Wprowadzone parzyste:', wybrane_parzyste)
print('Liczba tych liczb:', len(wybrane_parzyste))
