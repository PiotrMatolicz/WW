from klasy import *

osoba = Osoba('Ala', 'Kowalska', 30)
student = Student('Jan', 'Kowalski', 22, 'medycyna', 3)

print(osoba)
print(student)

# Osoba oraz Student posiadają atrybuty i metody zdefiniowane w klasie Osoba
print(osoba.imie, osoba.nazwisko)
print(student.imie, student.nazwisko)

print(osoba.pelnoletnia(), student.pelnoletnia())

# Ale tylko Student posiada atrybuty oraz metody dodane w klasie Student
#ERR print(osoba.kierunek, osoba.srednia_ocen())

student.dodaj_ocene(5)
student.dodaj_ocene(3)
student.dodaj_ocene(3)

print(student.kierunek, student.srednia_ocen())
print()

# Jeśli w nadklasie i podklasie jakaś metoda jest zdefiniowana w różny sposób (mamy tzw. overriding)
# to takie samo wywołanie może dać różny efekt w zależności od typu obiektu:
osoba.przedstaw_sie()
student.przedstaw_sie()
print()

# Jeśli obiekty różnych klas wymieszamy ze sobą, np. w jednej liście...
pacjenci = [
    osoba,
    student,
    Student('Adam', 'Abacki', 20, 'informatyka', 1),
    Osoba('Józef', 'Piłsudski', 80),
]

for x in pacjenci:
    print('Do lekarza przyszła jakaś osoba:', x)
    x.przedstaw_sie()
    print()

# Praktyczne zastosowania overridingu (pokrewne słowo: polimorfizm)
# np. tak sama operacja na zwykłym słowniku działa inaczej, a na defaultdict inaczej
# zapytanie do bazy Oracle wysyła się w jeden sposób, a do bazy PostgreSQL w inny sposób
