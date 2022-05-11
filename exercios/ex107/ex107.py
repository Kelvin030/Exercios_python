import moeda
valor = float(input("Digite uma valor:R$ "))
print(f'A metade de R${valor} é de R${moeda.metade(valor)} ')
print(f'O dobro de R${valor} é de R${moeda.dobro(valor)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(10, valor)}')
