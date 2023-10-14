a = 1
b = 2

def foo():
    global a
    a=2
    print("przesten funkcji", a, b)

foo()
print("globalna przestrzen", a, b)

