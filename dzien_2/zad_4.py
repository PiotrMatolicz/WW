"""
Stwórz tuplę zawierającą 10 różnych liczb całkowitych.
Korzystając z operatora dostępu oraz wycinania pobierz:
- drugi element (20)
- przedostatni element (90)
- elementy od trzeciego do siódmego (włącznie) (30, 40, 50, 60, 70)
- co trzeci element (10, 40, 70, 100)
- co drugi element licząc od końca (100, 80, 60, 40, 20)
"""
#         0   1   2   3   4   5   6   7   8   9
liczby = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
#         -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

print(liczby[1])  # 20
print(liczby[-2])  # 90
print(liczby[2:7])  # 30, 40, 50, 60, 70
print(liczby[::3])  # 10, 40, 70, 100
print(liczby[::-2])  # 100, 80, 60, 40, 20
