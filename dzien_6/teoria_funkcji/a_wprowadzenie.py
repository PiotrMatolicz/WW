print('Początek programu')

# Definicja funkcji polega na tym, że Python wczytuje treść funkcji i ją sobie zapamiętuje,
# ale w tym momencie tej treści nie wykonuje.
def aaa():
    print('aaa, kotki dwa')
    print('poszły spać')

print('Funkcja aaa została zdefiniowana')

# Teraz Python już wie, że pod nazwą aaa kryje się funkcja zdefiniowana powyżej.
# Jeśli chcemy wykonać instrukcje zawarte w treści funkcji, to tę funkcję nalezy "wywołać" (invoke, call)
print('Zaraz dwa razy wywołam funkcję aaa')
aaa()
aaa()
# Samo wpisanie nazwy funkcji bez nawiasów wskazuje funkcję, ale jej nie uruchamia
print('Wypisuję zmienną aaa:', aaa)
print('Gotowe\n')

# Funkcja to jest fragment programu, któremu nadaliśmy nazwę i którego możemy wielokrotnie używać.

# Funkcja może przyjmować parametry
def bbb(imie, wiek):
    print(f'Witamy osobę {imie}, która ma {wiek} lat.')
    if wiek < 18:
        print('  Jest to osoba niepełnoletnia')


print('Testowanie funkcji bbb:')
bbb('Ala', 20)
bbb('Jaś', 10)
bbb('Ola', 30)
print()
# Deklaracje i przekazywanie parametrów to w Pythonie b. rozbudowany temat - będzie oddzielny przykład.


# Funkcja może za pomocą instrukcji return zwracać wynik.
def ccc(miasto):
    if len(miasto) > 5:
        return f'Serdecznie pozdrawiamy miasto {miasto}'
    else:
        return f'Pozdrawiamy miasto {miasto}'


print('Testowanie ccc:')
ccc('Warszawa')
# Nie ma pozdrowień dla Warszawy
# Uwaga, uwaga! return to nie to samo co print
# Gdy funkcja za pomocą return "zwraca" wynik, to w miejscu wywołania decydujemy, co z tym wynikiem zrobić.
# Nie jest powiedziane, że on zostanie wydrukowany na ekran.

# Wynik funkcji można np. zapisać do zmiennej
zmienna = ccc('Kraków')
print('Wywołałem funkcję ccc dla parametru Kraków')
print('A wynikiem tego wywołania jest:', zmienna)

zmienna2 = ccc('Radom')
print('zmienna2:', zmienna2)

# wynik funkcji może być wykorzystany bezpośrednio w wyrażeniu,
# np. tutaj uzyskany napis pomnożymy przez 2
print(2 * ccc('Poznań'))

# W szczególności można wywołaniu funkcji umieścić bezpośrednio w print,
# ale działa to tak, że najpierw funkcja za pomocą return "zwraca" wynik, a dopiero potem print ten wynik wypisuje

print(ccc('Gdańsk'))
print()


def ddd():
    print('Nic tu nie ma')

# Jeśli jest zdefiniowana funkcja, ale nigdzie nie zostanie wywołana, to jej treść się nie wykona.

# Jedna funkcja może wywołać inną funkcję
def eee(imie, wiek, miasto):
    bbb(imie, wiek)
    pozdrowienie = ccc(miasto)
    print(pozdrowienie)


eee('Ula', 30, 'Łódź')
eee('Adam', 40, 'Szczecin')

