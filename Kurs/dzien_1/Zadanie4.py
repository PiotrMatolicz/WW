liczba=int(input("Podaj liczbe: "))

print(f"Większa od 10: {liczba >10}")
print(f"Mniejsza od 15: {liczba <15}")
print(f"liczba podzielna przez 2: {(liczba % 2==0) }")
wynik=(liczba % 3 !=0 and liczba % 3 ==0 and liczba < 10 ) or liczba==7
print(f"Wynik: {wynik}")