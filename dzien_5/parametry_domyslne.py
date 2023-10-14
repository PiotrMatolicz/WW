def zapisz_na_kurs(imie, tytul='Programowanie w Pythonie', miasto='Warszawa', ile_dni=10):
    print(f'Osoba {imie} zapisała się na kurs "{tytul}".')
    print(f'Kurs odbędzie się w mieście {miasto} i potrwa {ile_dni} dni.')
    print()


zapisz_na_kurs('Ala', 'Nauka programowania w Javie', 'Gdańsk', 8)

# można pominąć pewną liczbę parametrów na końcu - zostaną wtedy przyjęte wartości domyślne:
zapisz_na_kurs('Jacek', 'Kuchnia włoska')

zapisz_na_kurs('Patryk', 'Programowanie w C#', 'Wrocław')

# a co zrobić, aby podać inną liczbę dni, ale skorzystać z domyślnego tytułu i miasta?
zapisz_na_kurs('Aleksandra', ile_dni=20)

