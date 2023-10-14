"""
Korzystając z przypisywania wartości do zmiennych,
napisz program obliczający pole trapezu
o długości podstaw 3 i 9 oraz wysokości 6.5.
"""

podstaw_1 = 3
podstawa_2 = 9
wysokosc = 6.5

# https://docs.python.org/3/reference/expressions.html#operator-precedence
pole_trapezu = 0.5 * (podstaw_1 + podstawa_2) * wysokosc

print(pole_trapezu)
