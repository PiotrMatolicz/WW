x=float(input("Podaj położenie x: "))
y=float(input("Podaj położenie y: "))

if 10 >= x >= 0 and y <= 10 and y >= 0:
    print("Jesteś w lewym dolnym rogu")
elif 10 > x >= 0 and y<=90 and y>=10:
    print("Jesteś na lewym boku")
elif 10 >= x >= 0 and y <= 100 and y >= 90:
    print("Jesteś w lewym górnym rogu")
elif 90 >= x >= 10 and y<= 100 and y>= 90:
    print("Jesteś na górnym boku")
elif 100 >= x >= 90 and y <= 100 and y >= 90:
    print("Jesteś w prawym górnym rogu")
elif 100 >= x >= 90 and y<=90 and y>=10:
    print("Jesteś na prawym boku")
elif 100 >= x >= 90 and y<=10 and y>=0:
    print("Jesteś w prawym dolnym rogu")
elif 90 >= x >= 10 and y <= 10 and y>= 0:
    print("Jesteś na dolnym boku")
elif 10 <= x <= 90 and y <= 90 and y >= 10:
    print("Jesteś w środku")
else: print("Jesteś poza planszą")
