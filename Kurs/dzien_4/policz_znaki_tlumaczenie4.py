# Tutaj na początku do słownika wpisujemy wszystkie znaki występujące w napisie z wartością 0,
# a następnie zwiększamy o 1 za każdym razem, gdy widzimy znak.

napis = input('Wprowadź napis:\n')

znaki = {znak: 0 for znak in napis}

for znak in napis:
    znaki[znak] += 1

print(znaki)
