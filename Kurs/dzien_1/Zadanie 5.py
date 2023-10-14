rok_urodzenia=int(input("Podaj rok urodzenia: "))
aktualny_rok=int(input("Podaj aktualny rok: "))
wiek= aktualny_rok-rok_urodzenia
if wiek >=18:
    print("Jesteś pełnoletni")
else: print("Nie jesteś pełnoletni")