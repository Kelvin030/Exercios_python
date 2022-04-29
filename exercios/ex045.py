from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('faz sua escolha: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
print('-='*15)
print(f'O computador jogou:{itens[computador]}')
print(f'E você:{itens[jogador]}')
print('-='*15)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('O JOGADOR GANHOU!!!')
    elif jogador == 2:
        print('jogador PERDEU')
    else:
        print('JOGADA INVALIDA, tenete novamente')
elif computador == 1:
    if jogador == 0:
        print('o jogador PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('O JOGADOR GANHOU!!!')
    else:
        print('JOGADA INVALIDA, tenete novamente')
elif computador == 2:
    if jogador == 0:
        print('O JOGADOR GANHOU!!!')
    elif jogador == 1:
        print('jogador PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA, tenete novamente')
