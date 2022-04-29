print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('digite o valor a ser sacado: R$'))
céd = 50
totcéd = 0
total = valor
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'total de {totcéd} notas de R${céd}')
        if céd == 50:
                céd = 20
                totcéd = 0
        elif céd == 20:
                céd = 10
                totcéd = 0
        elif céd == 10:
                céd = 1
                totcéd = 0
        if total == 0:
            break
