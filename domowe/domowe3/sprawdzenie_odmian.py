from odmiana import Odmiana

print('Startujemy')
baza = Odmiana.wczytaj('PoliMorf-0.6.7.tab')
print('Baza odmian odmian wczytana')

a = baza.znajdzOdmiany('Tadeusz')
print(a)

b = baza.znajdzFormyPodstawowe('damy')
print(b)
