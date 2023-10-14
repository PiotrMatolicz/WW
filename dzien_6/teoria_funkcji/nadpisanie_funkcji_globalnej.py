# Ponieważ w Pythonie funkcje są traktowane na równi ze zmiennymi globalnymi,
# można omyłkowo nadpisać funkcję wbudowaną lub własną:

a = 5
b = 7
c = 4

max = max(a, b, c)
print('Maksymalna wartość to:', max)

x = 3.14
y = 77.7
z = 2**0.5 # pierwiastek z dwóch
max = max(x, y, z)
# błąd, bo teraz pod nazwą max nie mam już wbudowanej funkcji Pythona, tylko wartość 7
print('Maksymalna wartość to:', max)
