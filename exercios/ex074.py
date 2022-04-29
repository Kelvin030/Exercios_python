from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10),randint(1, 10))
for n in num:
    print(n, end=' ')
print(f'\nmaior:{max(num)}')
print(f'menor:{min(num)}')
