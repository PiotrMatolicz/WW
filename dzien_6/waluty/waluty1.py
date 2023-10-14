# W tej wersji dane JSON kopiujemy z przeglądarki i wklejamy tu jako kod Pythona.

dane = [{"table":"A","no":"174/A/NBP/2023","effectiveDate":"2023-09-08","rates":[{"currency":"bat (Tajlandia)","code":"THB","mid":0.1211},{"currency":"dolar amerykański","code":"USD","mid":4.2958},{"currency":"dolar australijski","code":"AUD","mid":2.7468},{"currency":"dolar Hongkongu","code":"HKD","mid":0.5481},{"currency":"dolar kanadyjski","code":"CAD","mid":3.1431},{"currency":"dolar nowozelandzki","code":"NZD","mid":2.5368},{"currency":"dolar singapurski","code":"SGD","mid":3.1505},{"currency":"euro","code":"EUR","mid":4.6019},{"currency":"forint (Węgry)","code":"HUF","mid":0.01195},{"currency":"frank szwajcarski","code":"CHF","mid":4.8225},{"currency":"funt szterling","code":"GBP","mid":5.3645},{"currency":"hrywna (Ukraina)","code":"UAH","mid":0.1163},{"currency":"jen (Japonia)","code":"JPY","mid":0.029143},{"currency":"korona czeska","code":"CZK","mid":0.1890},{"currency":"korona duńska","code":"DKK","mid":0.6169},{"currency":"korona islandzka","code":"ISK","mid":0.032024},{"currency":"korona norweska","code":"NOK","mid":0.4026},{"currency":"korona szwedzka","code":"SEK","mid":0.3863},{"currency":"lej rumuński","code":"RON","mid":0.9271},{"currency":"lew (Bułgaria)","code":"BGN","mid":2.3529},{"currency":"lira turecka","code":"TRY","mid":0.1600},{"currency":"nowy izraelski szekel","code":"ILS","mid":1.1189},{"currency":"peso chilijskie","code":"CLP","mid":0.004861},{"currency":"peso filipińskie","code":"PHP","mid":0.0758},{"currency":"peso meksykańskie","code":"MXN","mid":0.2459},{"currency":"rand (Republika Południowej Afryki)","code":"ZAR","mid":0.2250},{"currency":"real (Brazylia)","code":"BRL","mid":0.8630},{"currency":"ringgit (Malezja)","code":"MYR","mid":0.9187},{"currency":"rupia indonezyjska","code":"IDR","mid":0.00028031},{"currency":"rupia indyjska","code":"INR","mid":0.051767},{"currency":"won południowokoreański","code":"KRW","mid":0.003222},{"currency":"yuan renminbi (Chiny)","code":"CNY","mid":0.5856},{"currency":"SDR (MFW)","code":"XDR","mid":5.6723}]}]

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
    print(rate)
    # print(rate["code"], rate["currency"], rate["mid"])
