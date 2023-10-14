def max3(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c



wynik = max3(65, 99, 43)
print('Wynik:', wynik)

def suma(liczby):
    wynik = 0
    for liczba in liczby:
        wynik += liczba
    return wynik

def suma_parzystych(liczby,):
    wynik1=0
    for liczba in liczby:
        if liczba % 2 ==0:
            wynik1 += liczba
    return wynik1


print(suma([3,5,7]))
print(suma([22,44,100,-1,1]))
print(suma_parzystych([32,1,5,8,21,22]))
def silnia(n):
    if n > 1:
        return n * silnia ( n - 1 )
    return n