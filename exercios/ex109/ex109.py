from moeda import *
valor = float(input("Digite uma valor:R$ "))
print(f'A metade de {moeda(valor)} é de {metade(valor,True)} ')
print(f'O dobro de {moeda(valor)} é de {dobro(valor,True)}')
print(f'Aumentando 10%, temos {aumentar(10,valor,True)}')
print(f'Reduzindo 13%, temos {diminuir(13, valor, True)}')
