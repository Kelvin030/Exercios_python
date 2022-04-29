from random import shuffle
n1 = str(input('digite o primeiro nome: '))
n2 = str(input('digite o segundo nome: '))
n3 = str(input('digite o terceiro nome: '))
n4 = str(input('digite o quarto nome: '))
list = [n1, n2, n3, n4]
shuffle(list)
print(f'a ordem dos ganhadores é : {list}')