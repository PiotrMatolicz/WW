# a = True
# b = False
# print(type(a))
a = 3
print(a == 3)
print(a != 3)
print(a < 4)
print(a <= 3)
print(a > 4)
print(a >= 3)
print(1 + 2 == 3)
print()

print("and")
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print("or")
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print("not")
print(not True) # False
print(not False) # True

liczba = 13
print(liczba % 2 != 0 and liczba > 10)

from random import randint

x = randint(1, 100)
y = randint(1, 100)
print('Wylosowane liczby:', x, y)

# spójniki logiczne: and , or, not
if x >= 50 and y >= 50:
    print('obie liczby >= 50')
else:
    print('co najmniej jedna liczba < 50')

if x >= 50 or y >= 50:
    print('co najmniej jedna liczba >= 50')
else:
    print('obie liczby < 50')

# Spójniki logiczne są 'leniwe'
# przykładowo zmienna b nie istnieje, a warunek się wykona bez błędu:
a = 40
if a > 10 or b > 10:
    print('OK')

# W połączeniu z faktem, że inne wartości mogą być traktowane jak wartości logiczne, daje to ciekawe zastosowania:
a = ''
b = 'Python'
c = 'Java'
# wypisze się pierwsza z tych wartości, która nie jest pusta
print(a or b)
print(b or c)

