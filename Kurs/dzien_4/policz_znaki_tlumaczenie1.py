# Gdybyśmy mogli dla każdego znaku, którego się spodziewamy, stworzyć sobie oddzielną zmienną,
# to policzbyśmy liczbę wystąpień w taki sposób:

napis = input('Wprowadź napis:\n')

ileA = 0
ileB = 0
ileC = 0

for znak in napis:
    if znak == 'a': ileA += 1
    if znak == 'b': ileB += 1
    if znak == 'c': ileC += 1
    # itd....

print(ileA, ileB, ileC)
