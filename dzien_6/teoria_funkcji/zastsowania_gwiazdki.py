miasta = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań']

print(*miasta, sep=';')
#print(miasta, sep=';')


from random import randint

zakres = (1, 10)
# zamiast pisać tak lub tak:
# x = randint(1, 10)
# x = randint(zakres[0], zakres[1])

# można w stylu "pajtonicznym":
x = randint(*zakres)
y = randint(*zakres)
print('Wylosowane liczby:', x, y)
