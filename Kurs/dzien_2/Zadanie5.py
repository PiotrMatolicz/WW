dane=[]
while len(dane) < 10  :
    x= float(input("Podaj liczbę: "))
    dane.append(x)

srednia=sum(dane)/len(dane)
print(f"średnia z wprowadzonych liczb to: {srednia}")