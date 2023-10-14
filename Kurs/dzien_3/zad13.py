# lista zawierająca liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1
lista = [x / 10 for x in range(0, 11)]
print(lista)

# zbiór tupli zawierających 3 elementy - daną liczbę, jej kwadrat i jej sześcian - w przedziale od -10 do 10
zbior = {(x, x*x, x*x*x) for x in range(-10, 11)}
print(zbior)

# słownik mapujący napisy na ich długość powstały ze zbioru napisów
napisy = ['Ala', 'Ewelina', 'Jan', 'Marek']
slownik = {napis : len(napis) for napis in napisy}
print(slownik)