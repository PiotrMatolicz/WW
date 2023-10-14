napis = input('Podaj napis: ')

samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
ile_samoglosek = 0

for litera in napis.lower():
    if litera in samogloski:
        ile_samoglosek += 1

print(f"W napisie '{napis}' jest {ile_samoglosek} samogłosek.")

######################

napis = input('Podaj napis: ')
napis_lower = napis.lower()

samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
ile_samoglosek = 0

for samogloska in samogloski:
    ile_samoglosek += napis_lower.count(samogloska)

print(f"W napisie '{napis}' jest {ile_samoglosek} samogłosek.")