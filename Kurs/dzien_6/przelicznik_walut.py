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

from dzien_6.waluty3 import rates

ADRES = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=json'
dane = requests.get(ADRES).json()






for rate in rates:
    print(rate["code"], rate["currency"], rate["mid"])