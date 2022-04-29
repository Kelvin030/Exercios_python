from random import randint
from time import sleep
n = randint(0, 10)
cout = 0
print('=' * 25)
print('Jogo da Adivinhação v2.0')
print('=' * 25)
sleep(1)
print('Computador:Pensei em uma numero enter 0 e 10 tenete adivinhar')
sleep(1)
r = int(input('seu palpite: '))
while r != n:
    if r < n:
        print('mais... tenete novamente')
        r = int(input('seu palpite: '))
        cout += 1
        sleep(0.2)
    if r > n:
        print('menos... tente novamente')
        r = int(input('seu palpite: '))
        cout +=1
        sleep(0.2)
print(f'PARABENS você acertou com {cout + 1} tentavivas')
