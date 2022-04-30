from random import randint
test = []
cont = 1
jogadores = {
    'jogador 1':randint(1,6),
    'jogador 2':randint(1,6),
    'jogador 3':randint(1,6),
    'jogador 4':randint(1,6),
}
for key, value in jogadores.items():
    print(f'O {key}, tirou {value}')

print()
print(" Ranking dos jogadores ".center(30,"="))
print()

