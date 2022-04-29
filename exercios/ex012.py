a1 = float(input('digite o valor do produto: R$'))
d = float(input('digite o porcentagem do desconto: '))
a2 = a1/100*d
a3 = a1 - a2
print(f'seu produto com {d}% de desconto vale: R${a3 :.2f}')
print(f'o valor descontado é R${a2 :.2f}')
