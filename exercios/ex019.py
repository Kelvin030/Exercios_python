from random import choice
n1 = str(input('digite o primeito nome: '))
n2 = str(input('digite o sengundo nome: '))
n3 = str(input('o terceiro nome: '))
n4 = str(input('e agora o quarto: '))
lista = [n1, n2, n3, n4]
print(f'o ganhador é {choice(lista)}')