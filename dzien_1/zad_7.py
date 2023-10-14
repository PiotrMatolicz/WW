"""
Napisz program, który na podstawie pozycji gracza (x, y) na planszy w przedziale od 0 do 100
wyświetli jego przybliżone położenie (centrum, prawy górny róg, górna krawędź, ...)
lub informację o pozycji poza planszą. Przyjmij wartość 10 jako margines krawędzi.

https://drive.google.com/file/d/1Ek18pnoqiGiDcZJT6RBT1yufPUMaMJ7N/view

Przykładowy komunikat programu:
Podaj pozycję gracza X: 95
Podaj pozycję gracza Y: 95
Gracz znajduje się w prawym górnym rogu.
"""

x = int(input('Podaj x: '))
y = int(input('Podaj y: '))

if 0 <= x <= 10:
    if 0 <= y <= 10:
        print('lewy dolny róg')
    elif 10 < y < 90:
        print('lewy bok')
    elif 90 <= y <= 100:
        print('lewy górny róg')
    else:
        print('Jesteś poza planszą')
elif 10 < x < 90:
    if 0 <= y <= 10:
        print('dolny róg')
    elif 10 < y < 90:
        print('środek')
    elif 90 <= y <= 100:
        print('górny róg')
    else:
        print('Jesteś poza planszą')
elif 90 <= x <= 100:
    if 0 <= y <= 10:
        print('prawy dolny róg')
    elif 10 < y < 90:
        print('prawy bok')
    elif 90 <= y <= 100:
        print('prawy górny róg')
    else:
        print('Jesteś poza planszą')
else:
    print('Jesteś poza planszą')
