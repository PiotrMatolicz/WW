from geometria import *

menu='''
Wybierz figure:
K - kwadrat
P - prostokąt
O - koło
Q - koniec programu
'''


while True:
    print(menu)
    wybor = input(': ').upper()
    if wybor== 'Q':
        break
    elif wybor == 'K':
        a=float(input('Podaj długość boku: '))
        pole = pole_kwadratu(a)
        obw = obwod_kwadratu(a)
        print(f'Pole wynosi {pole}, a obwód {obw}')
    elif wybor=='P':
        a=float(input('Podaj długość boku: '))
        b = float(input('Podaj długość boku: '))
        pole = pole_prostokąta(a,b)
        obw = obwod_prostokąta(a,b)
        print(f'Pole wynosi {pole}, a obwód {obw}')
    elif wybor == 'O' :
        a = float(input('Podaj długość promienia: '))
        pole = pole_koła(a)
        obw = obwod_koła(a)
        print(f'Pole wynosi {pole:.2f}, a obwód {obw:.2f}')
