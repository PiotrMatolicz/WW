"""
Napis program, który wyświetli wynik mnożenia dwóch liczb z zakresu 1-10.

Wynik programu:
1*1=1
1*2=2
...
3*4=12
...
10*10=100
"""

for a in range(1, 11):
    for b in range(1, 11):
        print(f"{a} * {b} = {a * b}")
