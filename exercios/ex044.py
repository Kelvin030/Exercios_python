v = float(input('digite o valor do produto: '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] DINHEIRO/CHEQUE
[ 2 ] CARTAO
''')
p = int(input('informe o modo de pagamento: '))
if p == 1:
    d = (v * 10) / 100
    print(f'o valor de R${v :.2f} com 10% desconto, ficará R${v - d :.2f}')
elif p == 2:
    f = int(input('digite a quantidade de prestaçôes: '))
    if f == 1:
        d = (v * 5) / 100
        print(f'o valor de R${v :.2f} com 5% desconto, ficará R${v - d :.2f}')
        print(f'valor de cada parcela {v / f :.2f}')
    elif f == 2:
        print(f'o valor de R${v :.2f} o produto não tera desconto')
        print(f'valor de cada parcela {v / f :.2f}')
    else:
        j = (v * 20) / 100
        print(f'o valor de R${v :.2f} com 20% juros, ficará R${j + v :.2f}')
        print(f'valor de cada parcela R${v / f :.2f}')
else:
    print('numero invalido tente novamente')
