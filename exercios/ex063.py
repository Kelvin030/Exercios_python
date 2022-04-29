print('=' * 27)
print('Seguência de fibonacci V1.0')
print('=' * 27)
quantidade = int(input('digite quantos termos você quer ver: '))
cont = 0
a, b = 0, 1
while cont != quantidade:
    print(a, end=' ➥ ')
    a, b = b, b+a
    cont += 1
print('FIM')
