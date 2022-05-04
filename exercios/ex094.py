geral = []
pessoa = {}
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    while True:
        pessoa['sexo'] = str(input('Sexo:[F/M] ')).upper()[0]
        if pessoa['sexo'] in "FM":
            break
        print("-" * 60)
        print("ERRO!!! Digite apenas F ou M...")
    geral.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp = str(input("Deseja continuar [S/N]")).upper()[0]
        if resp in "SN":
            break
        print("-" * 60)
        print("ERRO!!! Digite apenas S ou N...")
    if resp == "N":
        break
    print("-" * 60)
print("-=" * 30)

print(f"A) Foram cadastras {len(geral)} pessoas.")
media = soma / len(geral)
print(f"B) A media das idades é {media:5.2f} anos.")
print("C) As mulheres cadastras são ", end='')
for p in geral:
    if p['sexo'] == "F":
        print(p['nome'],end=' ')
print()
print('D) Pessoas com idade acima da media: ')
for p in geral:
    if p['idade'] >= media:
        print(f'Nome: {p["nome"]} => Sexo: {p["sexo"]} => Idade: {p["idade"]}')
