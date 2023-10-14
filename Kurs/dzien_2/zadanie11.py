napis = input('Podaj napis: ')

if napis.count("<")  !=1 or napis.count(">") !=1 or napis.index("<") > napis.index(">"):
    print("Nieprawidłowy napis")
    exit()

zliczac=False
liczba_znaków=0
for litera in napis:
    if litera=="<":
        zliczac=True
    elif litera==">":
        zliczac=False
    elif zliczac is True:
        liczba_znaków +=1

print(f"Dla napisu {napis} znaleziono {liczba_znaków} znaków.")