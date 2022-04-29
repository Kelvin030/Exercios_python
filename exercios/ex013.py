v = float(input('digite o valor do salario do funcionario: R$'))
p = float(input('digite o valor de porcetagem de aumento : '))
d = v / 100 * p
aumento = d + v
print(f'o salario do funcionario de {v} com o aumento de {p}%, ira receber R${aumento :.2f}')
