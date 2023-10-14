"""
FizzBuzz

Wypisz liczby od 1 do 100, przy czym:
- liczby podzielne przez 3 zastąp słowem 'Fizz',
- liczby podzielne przez 5, zastąp słowem 'Buzz',
- natomiast liczby podzielne i przez 3 i przez 5 zastąp słowem ‘FizzBuzz’.
"""
for liczba in range(1, 101):
    if liczba % 3 == 0:
        if liczba % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif liczba % 5 == 0:
        print('Buzz')
    else:
        print(liczba)
