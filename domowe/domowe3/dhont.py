def dhont(wyniki, lmandatow):
    ilorazy = sorted(((glosy/i, glosy, -poz, partia)
                      for poz, (partia, glosy) in enumerate(wyniki.items())
                      for i in range(1, lmandatow+1)), reverse=True)
    mandaty = {partia: 0 for partia in wyniki.keys()}
    for i, (iloraz, glosy, poz, partia) in enumerate(ilorazy):
        if i >= lmandatow: break
        mandaty[partia] += 1
    return mandaty


def main():
    wyniki = {"czerwoni": 12000, "zieloni": 7000, "niebiescy": 5000, "pomarańczowi": 3000}
    mandaty = dhont(wyniki, 5)
    print(mandaty)
    assert mandaty == {"czerwoni": 3, "zieloni": 1, "niebiescy": 1, "pomarańczowi": 0}


if __name__ == '__main__':
    main()
