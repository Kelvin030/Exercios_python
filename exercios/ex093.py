jogadores = {'nome':'','gols':[] }
jogadores['nome'] = str(input('Nome do jogador: '))
quant_jogos = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
for j in range(0, quant_jogos):
    jogadores['gols'].append(int(input(f"Quantos gols na partida {j}: ")))
print("-=" * 30)
for k, v in jogadores.items():
    print(f'{k}: {v}',end=' ')
print(f'total: {sum(jogadores["gols"])}')
print("-=" * 30)
print(f"O campo de nome tem o valor {jogadores['nome']}")
print(f"O campo gols tem o valor {jogadores['gols']}")
print(f"O campo total tem o valor {sum(jogadores['gols'])}")
print("-=" * 30)
print(f"o jogar {jogadores['nome']} jogou {quant_jogos} jogos")
for j in range(0, quant_jogos):
    print(f"=> Na partida {j}, fez {jogadores['gols'][j]}")
print(f"E tem um total de {sum(jogadores['gols'])} gols")
