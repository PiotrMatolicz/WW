# Aby posotować dane, musimy mieć je wszystkie na raz w pamięci,
# najlepiej w formie listy. Dlatego wczytamy wszystkie linie za pomocą readlines.

print('Czytam plik...')
with open('pan_tadeusz.txt', mode='r', encoding='UTF-8') as wejscie:
    linie = wejscie.readlines()

# W tej wersji programu używamy domyślnego sposobu sortowania, który w przypadku napisów
# oznacza sortowania oparte o kody znaków.

print(f'Wczytałem {len(linie)} linii.')
print('Sortuję...')
linie.sort()

print('Zapisuję plik...')
with open('posortowany1.txt', mode='w', encoding='UTF-8') as wyjscie:
    wyjscie.writelines(linie)

print('Gotowe')
