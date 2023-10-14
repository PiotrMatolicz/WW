def proba(lista, napis, liczba):
    lista += ['Ola', 'Ela']
    napis += ' ma kota'
    liczba += 33
    print('na koniec funkcji:\n', lista, napis, liczba, '\n')


def main():
    lista = ['Ala', 'Ula']
    napis = 'Ala'
    liczba = 1000
    print('na początku:\n', lista, napis, liczba, '\n')
    proba(lista, napis, liczba)
    print('na końcu:\n', lista, napis, liczba)

# Tylko efekt zmiany listy jest widoczny, a str i int nie
# str, int - to są klasy NIEMUTOWALNE (immutable)
# obiekty tych klas nie mogą zmieniać swojego wewnątrznego stanu
# a operacje takie jak +, replace zwracają w wyniku nowy obiekt
# += dla napisów do zmiennej wpisuje adres nowego obiektu

main()
