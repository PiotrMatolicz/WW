# Zamiast tworzyć oddzielne zmienne dla każdego znaku, możemy stworzyć jeden słownik,
# w którym dla określonego znaku pamiętamy liczbę wystąpień.
# Słownik zawiera "tak jakby zmienne".

napis = input('Wprowadź napis:\n')

znaki = {'a': 0, 'b': 0, 'c': 0}

for znak in napis:
    if znak == 'a': znaki['a'] += 1
    if znak == 'b': znaki['b'] += 1
    if znak == 'c': znaki['c'] += 1
    # itd....

print(znaki)
