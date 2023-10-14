from datetime import datetime

# Aby uzyskać dostęp do pliku, należy "otworzyć" ten plik za pomocą funkcji open:
# https://docs.python.org/3/library/functions.html#open
plik1 = open('plik.txt')
print('Otwarty plik:', plik1)

# Teraz na różne sposoby można odczytywać treść tego pliku:
# Operacja read() wczytuje całą treść pliku jako pojedynczy obiekt str:
tresc = plik1.read()
print('Cała treść ma rozmiar:', len(tresc))
print(tresc)
print("========")

# Aby pokazać Wam kolejne możliwości, muszę cofnąć się na początek pliku:
plik1.seek(0)

# Operacje pozwalające odczytać fragment pliku.
# W praktyce niezbyt często stosowane... (ale podaję, bo tak często wygląda obsługa plików w innych językach)

# Odczyt określonej liczby znaków:
s = plik1.read(3)
print(s)
# Gdy czytamy coś z pliku, to przesuwamy taki "kursor" wyznaczający pozycję w tym pliku
# Kolejne polecenia czytają dalszą treść
s = plik1.read(3)
print(s)

# Wczytanie całej linii.
# Jeśli już jakieś znaki z tej linii wczytywaliśmy, to będzie to doczytanie końca tej linii.
linia = plik1.readline()
print('linia1:', linia)

linia = plik1.readline()
print('linia2:', linia)

# W Pythonie operacje czytania linii (readline, readlines, iteracja po liniach)
# zwracają linie wraz ze znakiem końca linii \n

print("========")
# wróćmy na początek pliku...
plik1.seek(0)

# Wczytaj listę wszystkich linii:
linie = plik1.readlines()
print('Wszystkie linie:', linie)

# wróćmy na początek pliku...
plik1.seek(0)
print("========")

# Aby odczytać wszystkie linie i dla każdej "coś zrobić", nie musimy stosować
# żadnej z powyższych operacji, bo w Pythonie pętla for zastosowana do otwartego pliku
# przejdzie przez wszystkie linie tego pliku.
# Operacja strip jest tutaj po to, aby z końca każdej linii wykasować niepotrzebny znak \n
for linia in plik1:
    print('Kolejna linia to:', linia.strip())

# Pliki należy zamykać, aby "zwolnić zasoby systemowe".
plik1.close()
print("========")

# NAJBARDZIEJ TYPOWY ZAPIS STOSOWANY W PYTHONIE
# wykorzystuje konstrukcję with, dzięki której pliki są automatycznie zamykane.
# Nie trzeba pisać close.
# Przy okazji zobaczmy, że funkcja open ma więcej parametrów.
# Podawanie kodowania znaków jest czasami konieczne.

with open('plik.txt', mode='r', encoding='UTF-8') as plik2:
    # wszystkie operacje na pliku wpisujemy wewnątrz bloku with
    for linia in plik2:
        print('!', linia.strip())

# Gdy (po prostu redukując wcięcie) wyjdziemy z bloku with,
# to Python automatycznie zamknie ten plik.
print('\nKoniec danych. Plik zamknięty.')

# Aby zapisać dane do pliku, należy otworzyć plik w trybie 'w'
# Następnie można dane zapisywać za pomocą metody write (ona nie dopisuje znaku nowej linii)
# albo za pomocą print z dodatkowym parametrem file

with open('nowy.txt', mode='w', encoding='UTF-8') as plik3:
    plik3.write('Pierwsza linia')
    plik3.write(' Ciąg dalszy pierwszej linii\n')
    plik3.write('Druga linia\n')
    plik3.writelines(['Trzecia\n', 'Czwarta\n'])
    # write obsługuje wyłącznie parametry typu str
    # plik3.write(123 * 3) # TypeError: write() argument must be str, not int
    print('Piąta linia', file=plik3)
    print('Ala', 'Ola', 123*3, datetime.now(), file=plik3)

print('Koniec programu')
