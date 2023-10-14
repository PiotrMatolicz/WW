"""
Godzina parkowania kosztuje 3 zł
Na początku użytkownik deklaruje ile godzin parkowania opłaca
Program oblicza ile będzie do zapłaty

Następnie W PĘTLI program powinien prosić o wrzucenie kolejnej monety
(użytkownik wpisuje liczbę całkowitą i naciska enter)
tak długo, aż zostania wpłacona wymagana suma.

Jeśli należy wydać resztę, to program pisze ile tej reszty.
"""

CENA = 3
czas = int(input('Ile godzin parkujesz? '))
do_zaplaty = CENA * czas
print(f'Do zapłaty będzie {do_zaplaty}')

suma_wplat = 0
while suma_wplat < do_zaplaty:
    print(f'Do tej pory wpłacono {suma_wplat}, pozostało jeszcze {do_zaplaty - suma_wplat}')
    # wczytujemy kolejną monetę
    moneta = int(input('wrzuć monetę: '))
    suma_wplat = suma_wplat + moneta
    # suma_wplat += moneta

if suma_wplat > do_zaplaty:
    print(f'Należy się reszta {suma_wplat - do_zaplaty}')

print('Szerokiej drogi')
