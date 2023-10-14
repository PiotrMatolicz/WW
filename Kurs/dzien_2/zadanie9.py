import random

print(' ' * 4, end='')
for i in range(0, 11):
    print(f"{i:4}", end='')

print()
print()

for a in range(0, 11):
    print(f"{a:<4}", end='')
    for b in range(0, 11):
        if random.randint(1, 100) % 4 == 0:
            print('  __', end='')
        else:
            print(f"{a * b:4}", end='')

    print()