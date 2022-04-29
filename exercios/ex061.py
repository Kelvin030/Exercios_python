termo = int(input('digite o TERMO: '))
razao = int(input('digite a RAZÂO: '))
cont = 1
while cont <= 10:
    print(f'{termo}', end=' ➔ ')
    termo += razao
    cont += 1
print('FIM')
