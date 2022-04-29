from time import sleep
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
opcão = 0
while opcão != 5:
    if opcão != 5:
        print('=' * 30)
        print('''opções:
        [ 1 ] SOMAR
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR
        [ 4 ] NOVOS NUMEROS
        [ 5 ] SAIR DO PROGRAMA''')
        opcão = int(input('digite outro valor: '))
        print('=' * 30)
        if opcão == 1:
            print(f'a soma de {n1} + {n2} = {n1 + n2}')
        elif opcão == 2:
            print(f'a A multiplicação de {n1} X {n2} = {n1 * n2}')
            sleep(1)
        elif opcão == 3:
            if n1 > n2:
                print(f'o maior numero é {n1}')
            else:
                print(f'o maior numero é {n2}')
        elif opcão == 4:
            n1 = int(input('digite o primeiro numero: '))
            n2 = int(input('digite o segundo numero: '))
            sleep(1)
        elif opcão == 5:
            print('Programa finalizado, volte sempre')
        else:
            print('opção invalida')
