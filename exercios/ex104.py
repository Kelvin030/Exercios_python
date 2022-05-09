def leiaint(pergunta):
    while True:
        num = input(f'{pergunta}: ')
        if num.isdecimal():
            break
        else:
            print('\033[1;31mERRO!!! Digite um numero inteiro valido\033[m')
    return num


# Programa Principal
n = leiaint('Digite um numero')
print(f'Você acabou de digitar {n}')
