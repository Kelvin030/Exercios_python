mais = homens = mulheres = 0
while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    print('-' * 25)
    while sexo not in 'MF':
        sexo = str(input('Sexo [M / F]: ')).strip().upper()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S / N]: ')).strip().upper()
    if idade > 18:
        mais += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade > 20:
        mulheres += 1
    if continuar == 'N':
        break
print(f'Ha {mais} pessoas maior de idade')
print(f'Ha {homens} homens cadastrados')
print(f'Ha {mulheres} mulheres com mais de 20 anos')
