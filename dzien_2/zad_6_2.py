"""
Napisz program zliczający wystąpienia liczb dodatnich i ujemnych w zadanej liście
liczb całkowitych.
"""

liczby = [1, 2, 3, -100, -10, 0, 4]
liczby_dodatnie = []
liczby_ujemne = []

for liczba in liczby:
    if liczba > 0:
        liczby_dodatnie.append(liczba)
    elif liczba < 0:
        liczby_ujemne.append(liczba)

print(f"Ujemnych: {len(liczby_ujemne)}, dodatnich: {len(liczby_dodatnie)}")
print(f"Ujemne: {liczby_ujemne}")
print(f"Dodatnie: {liczby_dodatnie}")
