def max3_v1(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b >= c:
            return b
        else:
            return c


def max3_v2(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= c:
        return b
    return c


def max3_v3(a, b, c):
    return a if a >= b and a >= c else b if b >= c else c


def pole_trojkata(a, b, c):
    from math import sqrt
    if a > b + c or b > a + c or c > a + b:
        raise ValueError('Podane boki nie tworzą trójkąta')
    p = (a+b+c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))


def palindrom_v1(napis):
    for i in range(len(napis) // 2):
        if napis[i] != napis[-1 - i]:
            return False
    # jeśli przejrzeliśmy wszystkie pozycje i nie znaleźliśmy żadnej niezgodności,
    # to znaczy, że wszystko się zgadzało i można zwrócić True
    return True


def palindrom_v2(napis):
    return napis == napis[::-1]


def statystyki(lista):
    cnt, sum, min, max = 0, 0, None, None
    for x in lista:
        cnt += 1
        sum += x
        if min is None or x < min:
            min = x
        if max is None or x > max:
            max = x
    avg = sum/cnt if cnt > 0 else None
    return cnt, sum, avg, min, max


def main():
    print(max3_v1(12, 19, 9))
    print(max3_v2(12, 19, 9))
    print(max3_v3(12, 19, 9))
    print(pole_trojkata(3, 4, 5))
    print(statystyki([11, 12, 13, 18, 17]))
    print(statystyki([]))
    print(statystyki(range(100, 200, 5)))


if __name__ == '__main__':
    main()
