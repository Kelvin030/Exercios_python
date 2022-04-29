dias = int(input('quantos dias o carro foi alugado: '))
km = float(input('quantos Km rodados: '))
total = float (60 * dias) + (0.15 * km)
print (f'O total a pegar é R${total :.2f}')