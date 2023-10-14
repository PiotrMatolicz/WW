'''
Napisz program, który sprawdza, czy podana liczba jest liczbą pierwszą.
'''

print('Aby przerwać, podaj -1')

while True:
    liczba = int(input('Podaj liczbę: '))
    if liczba < 0: break
    
    if liczba < 2:
        print(f'Liczba {liczba} NIE JEST liczbą pierwszą')
        continue
        
    for i in range(2, int(liczba**0.5)+1):
        if liczba % i == 0:
            print(f'Liczba {liczba} NIE JEST liczbą pierwszą')
            break
    else:
        print(f'Liczba {liczba} JEST liczbą pierwszą')
