s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
        cont = cont + 1
print('A soma de todos os numeros é de {}'.format(s))
print('{} numeros foram somados'.format(cont))
