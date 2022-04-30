from random import randint
test = []
cont = 1
jogadores = {
    'jogador1':randint(1,6),
    'jogador2':randint(1,6),
    'jogador3':randint(1,6),
    'jogador4':randint(1,6),
}
for key, value in jogadores.items():
    print(f'O {key}, tirou {value}')

print()
print(" Ranking dos jogadores ".center(30,"="))
print()
