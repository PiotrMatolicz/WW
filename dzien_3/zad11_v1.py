wejscie = input('Podaj liczby rozdzielone spacją:\n')
liczby = {int(x) for x in wejscie.split()}
parzyste = set(range(0, 101, 2))
print('Liczb spełniających warunek było:', len(liczby & parzyste))
