# W tej wersji zwiększamy liczbę wystąpień na tej pozycji, na którą wskazuje bieżący znak.
# To zadziała już prawidłowo, jeśli słownik zainicjujemy wszystkimi możliwymi znakami.

napis = input('Wprowadź napis:\n')

znaki = {'a': 0, 'b': 0, 'c': 0}

for znak in napis:
    if znak in znaki:
        znaki[znak] += 1

print(znaki)
