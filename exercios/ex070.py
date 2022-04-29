cont = mais1000 = soma = 0
print('=' * 20)
print('Loja De Um Real')
print('=' * 20)
while True:
    nome = str(input('NOME: '))
    preço = float(input('PREÇO: R$'))
    resp = ' '
    print('-' * 20)
    while resp not in 'SN':
        resp = str(input('quer continuar[S / N]: ')).strip().upper()[0]
    soma += preço
    cont += 1
    if preço >= 1000:
        mais1000 += 1
    if cont == 1:
        maisbarato = preço
        nome1 = nome
    if preço < maisbarato:
        maisbarato = preço
        nome1 = nome
    if resp == 'N':
        break
print('-' * 20)
print(f'O total da compra é \033[32mR${soma :.2f}\033[m')
print(f'Temos {mais1000} produtos acima de R$1000,00')
print(f'O produto mais barato é \033[32m{nome1}\033[m que vale \033[32mR${maisbarato :.2f}')
