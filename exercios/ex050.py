s = 0
cont = 0
for c in range(1, 7):
    n = int(input('digite um numero PAR: '))
    if n % 2 == 0:
        s += n
        cont += +1
print(f'a soma {cont} PARES é ingual a {s}')
