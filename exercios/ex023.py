#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
n = int(input('digite um numero: '))
n1 = n // 1 % 10
n2 = n // 10 % 10
n3 = n // 100 % 10
n4 = n // 1000 %  10
print(f'unidade:{n1}\ndezena:{n2}\ncentena:{n3}\nmilhar:{n4}')