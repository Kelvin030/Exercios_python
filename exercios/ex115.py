# Desafio: Criar uma calculadora utilizando class
class Calculadora:
    def __init__(self):
        pass

    def adição(self, a=1, b=1):
        return a + b

    def subtração(self, a=1, b=1):
        return a - b

    def multiplicação(self, a=1, b=1):
        return a * b

    def divisão(self, a=1, b=1):
        return a / b


calculadora = Calculadora()
while True:
    print('=' * 40)
    print('Calculadora'.center(40))
    print('=' * 40)
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')
    print('=' * 40)

    while True:
        try:
            opção = int(input('Sua opção: '))
        except:
            print('ERRO! Tente novamente')
        else:
            break

    while True:
        try:
            num1 = int(input('Primeiro valor: '))
            num2 = int(input('Segundo valor: '))
        except:
            print('ERRO! Tente novamente')
        else:
            break

    if opção == 1:
        print(f'{num1} + {num2} = {calculadora.adição(num1, num2)}')
    elif opção == 2:
        print(f'{num1} - {num2} = {calculadora.subtração(num1, num2)}')
    elif opção == 3:
        print(f'{num1} X {num2} = {calculadora.multiplicação(num1, num2)}')
    elif opção == 4:
        print(f'{num1} / {num2} = {calculadora.divisão(num1, num2)}')
    elif opção == 5:
        break
    else:
        print('Opção digitada invalida')
    