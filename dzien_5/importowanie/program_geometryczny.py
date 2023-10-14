# from geometria import pole_kwadratu, obwod_kwadratu
from geometria import *

menu = '''
Wybierz figurę:
K - kwadrat
P - prostokąt
O - koło
Q - koniec programu'''

while True:
    print(menu)
    wybor = input(': ').upper()
    if wybor == 'Q':
        break
    elif wybor == 'K':
        a = float(input('Podaj długość boku: '))
        pole = pole_kwadratu(a)
        obw = obwod_kwadratu(a)
        print(f'Pole wynosi {pole}, a obwód {obw}')
    elif wybor == 'P':
        a = float(input('Podaj długość pierwszego boku: '))
        b = float(input('Podaj długość drugiego boku: '))
        pole = pole_prostokata(a, b)
        obw = obwod_prostokata(a, b)
        print(f'Pole wynosi {pole}, a obwód {obw}')
    elif wybor == 'O':
        r = float(input('Podaj promień koła: '))
        pole = pole_kola(r)
        obw = obwod_kola(r)
        print(f'Pole wynosi {pole}, a obwód {obw}')
    else:
        print('Nieznana opcja')
