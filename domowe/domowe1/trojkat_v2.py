'''
Napisz program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.
'''

boki = []
for i in range(3):
    boki.append(float(input(f'Podaj długość boku nr {i+1}: ')))

p = sum(boki) / 2
if max(boki) > p:
    print('To nie jest poprawny trójkąt')
else:
    iloczyn = p
    for x in (p - bok for bok in boki):
        iloczyn *= x
    pole = iloczyn**0.5
    print(f'To jest poprawny trójkąt, a jego pole wynosi {pole}')
