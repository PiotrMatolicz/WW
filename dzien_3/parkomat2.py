# Zamiast dodawać monety do suma_wplat, w tej wersji odejmuję je od do_zaplaty
# Wychodzi nieco krótszy zapis, ale nie ma na bieżąco informacji ile wpłacono do tej pory.

CENA = 3
czas = int(input('Ile godzin parkujesz? '))
do_zaplaty = CENA * czas
print(f'Do zapłaty będzie {do_zaplaty}')

# dopóki pozostało coś jeszcze do zapłaty
while do_zaplaty > 0:
    print(f'Pozostało jeszcze {do_zaplaty}')
    do_zaplaty -= int(input('wrzuć monetę: '))

if do_zaplaty < 0:
    print(f'Należy się reszta {-do_zaplaty}')

print('Szerokiej drogi')
