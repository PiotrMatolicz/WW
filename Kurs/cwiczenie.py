liczby = [7, 3, 12, 5, 14, 8, 9]
indeks = 0
liczba = liczby[0]
while indeks < len(liczby) and (liczba := liczby[indeks]) <= 10:
        indeks +=1


if indeks < len(liczby):
       print(f"Pierwsza liczba większa od 10 to {liczba}, znajdująca się na pozycji {indeks}.")

else:
       print("Nie znaleziono liczby większej od 10 w liście.")





