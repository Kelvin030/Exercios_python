import moeda
valor = float(input("Digite uma valor:R$ "))
print(f'A metade de {moeda.moeda(valor)} é de {moeda.moeda(moeda.metade(valor))} ')
print(f'O dobro de {moeda.moeda(valor)} é de {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(10, valor))}')
