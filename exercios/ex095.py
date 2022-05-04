time = []
jogadores = {'nome':'','gol':[]}

while True:
    jogadores['nome'] = str(input("Nome do jogador: "))
    qunt_jogos = int(input(f"Quando jogos {jogadores['nome']} Jogou? "))

    for x in range(0,qunt_jogos):
        jogadores['gol'].append(int(input(f"Quantos gols na partida {x}: ")))
    time.append(jogadores.copy())
    jogadores.clear()

    while True:
        resp = str(input("Deseja continuar [S/N]")).upper()[0]
        if resp in "SN":
            break
        else:
            print("Digite apenas S ou N...")

print("=-" * 30)
print(time)
