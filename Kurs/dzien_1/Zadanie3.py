#Napisz program obliczający koszt przejazdu z miasta A do B na podstawie podanej
#przez użytkownika liczby kilometrów, ceny paliwa oraz spalania.
#Zapytaj użytkownika także o nazwy miejscowości.

#Jak to policzyć?
#koszt = dystans * spalanie / 100.0 * cena_paliwa
#koszt = 420 * 5.5 / 100.0 * 4.55

#Przykładowe komunikaty programu:
#Podaj miasto A: Warszawa
#Podaj miasto B: Gdańsk
#Podaj dystans Warszawa-Gdańsk: 420
#Podaj cenę paliwa: 4.55
#Podaj spalanie na 100 km: 5.5
#Koszt przejazdu Warszawa-Gdańsk to 105.11 PLN
a = input("Podaj miasto a: ")
b = input("Podaj miasto b: ")
c = int(input(f"Podaj dystans między{a}-{b}: "))
d = float(input("Podaj cene paliwa: "))
e = float(input("Podaj saplanie na 100km: "))
koszt = c * e / 100.0* d

print(f"Koszt przejazdu{a}-{b}to {koszt:.2f} PLN ")