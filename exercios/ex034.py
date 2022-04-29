salario = float(input('digite a valor do salario: R$'))
if salario > 1250.00:
    resultado = (salario / 100) * 10 + salario
else:
    resultado = (salario / 100) * 15
print(f'o salario de R${salario :.2f} foi para R${resultado :.2f}')
