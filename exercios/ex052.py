n = int(input('digite um numero: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[31m', end=' ')
        tot += 1
    else:
        print('\033[32m', end=' ')
    print(c, end='')
print(f'\n\033[mo numero {n} e divisivel {tot} vezes')
if tot == 2:
    print(f'\n\033[mo número {n} é um número PRIMO')
else:
    print(f'\n\033[mo número {n} NÂO é um número primo')
