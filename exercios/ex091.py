from random import randint
from time import sleep
from operator import itemgetter
test = []
cont = 1
jogadores = {
    'Jogador1':randint(1,6),
    'Jogador2':randint(1,6),
    'Jogador3':randint(1,6),
    'Jogador4':randint(1,6),
}
for key, value in jogadores.items():
    print(f'O {key}, tirou {value}')
    sleep(0.5)

print()
print(" Ranking dos jogadores ".center(30,"="))
print()

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for c, v in enumerate(ranking):
    print(f'{c+1}º Lugar: {v[0]} com {v[1]} pontos')
    sleep(1)
