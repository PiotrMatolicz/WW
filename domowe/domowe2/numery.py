# etap 1 - wygeneruj listę numerów telefonów

# elementami byłby liczby (wartości int):
# numery = [x for x in range(48123001000, 48123006000)]

# numery = [f'+4812300{x}{y1}{y2}{y3}'
#           for x in range(1, 6)
#           for y1 in range(0, 10)
#           for y2 in range(0, 10)
#           for y3 in range(0, 10)]

numery = [f'+4812300{x}' for x in range(1000, 6000)]

print(numery[0], numery[-1], 'rozmiar listy:', len(numery))
print()

# etap 2 - wylosuj 10 elementów
import random

for numer in random.sample(numery, 10):
    print(numer)
