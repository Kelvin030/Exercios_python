num = (int(input('digte um número: ')),
       int(input('digte outro número: ')),
       int(input('digte mais um número: ')),
       int(input('digte o ultimo numero: ')))
print(f'vc digitou os valores: {num}')
print(f'apareceu {num.count(9)} vezes o número 9')
if 3 in num:
    print(f'o numero 3 apareceu na posição {num.index(3)}')
print('os numeros pares digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
