primeiro = int(input('digite o termo: '))
razao = int(input('digite a razao: '))
cont = 1
termo = primeiro
n = 10
total = 0
while n != 0:
    total += n
    while cont <= total:
        print(termo, end=' ➔ ')
        print('PAUSA')
        termo += razao
        cont += 1
    n = int(input('\ndigite quantos mais termos vc quer ver? '))
print(f'foram gerados {total} TERMOS')
