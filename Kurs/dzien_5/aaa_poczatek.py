def wejdz_do_szafy(osoby):
    if len(osoby)==1:
        print(f"{osoby[0]} wchodzi do szafy")
    else:
        print(f"{', '.join(osoby)} wchodzą do szafy")
        print("I znajdują się w Krainie Narni")
        print("Mają ciekawe przygody")
        print("I wracją do świata ludzi")

print("Początek programu")
print("Łucja wchodzi do pokoju z szafą")
wejdz_do_szafy(["Łucja"])
print("Wraca do rodzeństwa i opowiada co ją spotkało")
print()
print("Edmund też chce zobaczyć,co tam jest")
wejdz_do_szafy(["Edmund"])
print("Po spotkaniu czrownicy wraca ale się do tego nie przyznaje")
print()
wejdz_do_szafy(["Łucja", "Edmund", "Zuzanna", "Piotr"])
print("Koniec programu")
