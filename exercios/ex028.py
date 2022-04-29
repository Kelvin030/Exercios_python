from random import randrange
from time import sleep
print('=-=-'*14)
print('Vou pensar um um numemo entre 0 e 5 tente adivinhar!!')
print('=-=-'*14)
n = randrange(0, 5)
r = int(input('digite um valor entre 0 e 5: '))
print('carregando...')
sleep(2)
if (r == n):
    print('Você Acertou!!!')
else:
    print(f'infelizmente você errou o valor era {n}')
