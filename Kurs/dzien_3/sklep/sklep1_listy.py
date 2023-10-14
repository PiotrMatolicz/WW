# W tej wersji dane towarów będziemy pamiętać w dwóch listach: nazwy oraz ceny
# w tej samej kolejności.

towary = ['pralka', 'odkurzacz', 'telewizor']
ceny = [2300, 400, 1900]

# Program wyświetla dostępne towary i w pętli pozwala wybrać towar,
# podać liczbę sztuk i wypisuje kwotę do zapłaty.
# Oblicza też sumę całkowitą.

print('Dostępne towary')

# Ta pętla wypisze same nazwy towarów:
# for towar in towary:
#     print(towar)

# A jak wypisać nr pozycji, nazwę oraz cenę?
# sposób 1: za pomocą indeksu idącego od 0 do len-1, jak w języku C...
# for i in range(len(towary)):
#     print(f'{i} : {towary[i]} za {ceny[i]} zł')
# print("="*30)


# sposób 2: za pomocą zip przeglądamy dwie listy w jednej pętli for,
# a enumerate generuje indeksy:
# for tupla in enumerate(zip(towary, ceny)):
#     print(tupla)
#     print(f'{tupla[0]} : {tupla[1][0]} za {tupla[1][1]} zł')

# dodatkowo stosując technikę rozpakowywania,
# możemy od razu wpisać wartości do zmiennych o sensownych nazwach:
for i, (towar, cena) in enumerate(zip(towary, ceny)):
    print(f'{i:2} : {towar:10} za {cena:8} zł')

koszt_sumaryczny = 0
while True:
    dane = input('Podaj numer wybranego towaru albo zakończ naciskając enter: ')
    if not dane: # jeśli dane są puste
        break
    nr = int(dane)
    print(f'Jedna sztuka towaru {towary[nr]} kosztuje {ceny[nr]} zł.')
    sztuk = int(input('Ile sztuk chcesz kupić? '))
    koszt = ceny[nr] * sztuk
    koszt_sumaryczny += koszt
    print(f'Za {sztuk} sztuk towaru {towary[nr]} płacisz {koszt} zł.')

print(f'Łącznie za zakupy płacisz {koszt_sumaryczny} zł')
