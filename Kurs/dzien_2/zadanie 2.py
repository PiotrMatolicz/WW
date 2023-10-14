numerdnia=1
suma=0
while numerdnia<=7:
    suma=float(input(f"Podaj temperature tego dnia {numerdnia}: "))
    numerdnia += 1
    średnia = suma/ 7
    if numerdnia >7:
        print(f"ŚREDNIA TEMPERATUR TO {średnia:.2f}")
