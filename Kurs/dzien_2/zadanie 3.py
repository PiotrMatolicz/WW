
xmax=None
xmin=None
while True :
    x= input("Podaj liczbę: ")
    if x == "koniec" :
        break

    x1=float(x)

    if xmin is None or x1<xmin:
       xmin=x1
    if xmax is None or x1> xmax:
       xmax=x1

print(f"Znalezione minimum: {xmin}")
print(f"Znalerzione maximum: {xmax}")