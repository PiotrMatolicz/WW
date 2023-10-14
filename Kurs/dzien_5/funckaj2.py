def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b
while True:
    arg= int(input( 'Podaj liczbę: '))
    if arg < 0 : break
    wynik = fib(arg)
    print(f'{arg} != {wynik}')