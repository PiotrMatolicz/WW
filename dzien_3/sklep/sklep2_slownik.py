# W tej wersji dane towarów będziemy pamiętać w słowniku,
# który dla nazwy towaru pamięta cenę tego towaru.
cennik = {
    'pralka': 2300,
    'odkurzacz': 400,
    'telewizor': 1900,
}

print('Dostępne towary')
# print(cennik)

# Ta pętla wypisze same nazwy towarów:
# for towar in cennik:
#     print(towar)

# Aby przejrzeć klucze wraz z wartościami, używa się metody items
# w połączeniu z techniką rozpakowywania
for nazwa, cena in cennik.items():
    print(f' * {nazwa} za {cena} zł')

koszt_sumaryczny = 0
while True:
    nazwa = input('Podaj nazwę wybranego towaru albo zakończ naciskając enter: ')
    if not nazwa: break
    if nazwa not in cennik:
        print(f'Nie istnieje towar o nazwie {nazwa}')
        continue
    print(f'Jedna sztuka towaru {nazwa} kosztuje {cennik[nazwa]} zł.')
    sztuk = int(input('Ile sztuk chcesz kupić? '))
    koszt = cennik[nazwa] * sztuk
    koszt_sumaryczny += koszt
    print(f'Za {sztuk} sztuk towaru {nazwa} płacisz {koszt} zł.')

print(f'Łącznie za zakupy płacisz {koszt_sumaryczny} zł')
