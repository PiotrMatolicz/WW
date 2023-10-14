# W tej wersji pobieramy dane prosto z sieci za pomocą biblioteki requests
import requests

ADRES = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=json'
dane = requests.get(ADRES).json()

print(dane)
print('typ zmiennej dane:', type(dane))

# lista zawiera jeden element, którym jest słownik
tabela = dane[0]
print('typ zmiennej tabela:', type(tabela))

print('Numer tabeli:', tabela["no"])
print('Data tabeli:', tabela["effectiveDate"])
print()

rates = tabela["rates"]
print('typ zmiennej rates:', type(rates))
print('liczba elementów:', len(rates))
print()

# Tutaj rate jest słownikiem, który pełni rolę obiektu.
# W tym słowniku są trzy pola: currency (nazwa waluty), code (kod 3-literowy), mid (kurs średni)
for rate in rates:
    print(rate["code"], rate["currency"], rate["mid"])