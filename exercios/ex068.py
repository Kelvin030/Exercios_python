from random import randint
impar = 1
par = cont = 0
while True:
    print('=' * 40)
    num = int(input('digite um valor: '))
    print('=' * 40)
    resposta = str(input('escolha IMPAR ou PAR [I / P]: ')).strip().upper()[0]
    print('=' * 20)
    computador = randint(0, 10)
    if resposta == 'I':
        soma = computador + num
        if soma % 2 == impar:
            print('você venceu')
            print(f'o computador jogou {computador} e o jogador {num} a soma é {soma}')
            print('=' * 40)
            cont += 1
        else:
            print('você perdeu')
            print(f'o computador jogou {computador} e o jogador {num} a soma é {soma}')
            print('=' * 40)
            break
    if resposta == 'P':
        soma = num + computador
        if soma % 2 == par:
            print('você venceu')
            print(f'o computador jogou {computador} e o jogador {num} a soma é {soma}')
            print('=' * 40)
            cont += 1
        else:
            print('você perdeu')
            print(f'o computador jogou {computador} e o jogador {num} a soma é {soma}')
            print('=' * 40)
            break
print(f'você ganhou {cont} vezes')
print('Obrigado por jogar')
