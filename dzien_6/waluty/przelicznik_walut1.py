'''
Napisz program, który:
- pobiera najnowszą tabelę kursów NBP
w pętli:
- pozwala użytkownikowi podać kod waluty (np. USD)
- wypisuje dane tej waluty (nazwę oraz kurs)
- pozwala wpisać liczbę
- przelicza podaną kwotę w walucie na złote (i ew. w drugą stronę też)
'''
import requests

ADRES = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=json'
dane = requests.get(ADRES).json()
tabela = dane[0]
rates = tabela["rates"]
print(f'Tabela {tabela["no"]} z dnia {tabela["effectiveDate"]}. {len(rates)} walut')

while True:
    kod = input('Podaj kod waluty: ').strip().upper()
    if not kod: break
    for rate in rates:
        if rate["code"] == kod:
            print(rate)
            mid = rate["mid"]
            kwota = float(input('Podaj kwotę: '))
            print(f'{kwota:.2f} {kod} = {kwota * mid:.2f} PLN')
            print(f'{kwota:.2f} PLN = {kwota / mid:.2f} {kod}')
            print()
            break
    else:
        print(f'Nie istnieje waluta o kodzie {kod}')

