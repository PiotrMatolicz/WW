"""
Napisz program zliczający liczbę wystąpień samogłosek (a, e, i, o, u, y)
w podanym przez użytkownika napisie.

1. Pobieramy napis od użytkownika
2. Przechodzimy po każdej literze z napisu (for)
3. Sprawdzamy, czy znak znajduje się w samogłoskach -> jeśli tak, to go zliczamy

Jak poradzić sobie ze zliczaniem dużych liter?
1. Możemy je dodać do tupli z samogłoskami
2. Użyć metody .lower()
"""

napis = input('Podaj napis: ')
napis_lower = napis.lower()

samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
ile_samoglosek = 0

for samogloska in samogloski:
    ile_samoglosek += napis_lower.count(samogloska)

print(f"W napisie '{napis}' jest {ile_samoglosek} samogłosek.")
