list = []
while True:
    valor = list.append(int(input("digite um valor: ")))
    if valor not in list:
        print('valor adicionado...')
    else:
        list.pop()
        print('esse valor já foi adicionado...')
    resposta = input('deseja continuar? [S/N] ').upper()
    if resposta == 'N':
        break
list.sort()
print(f"Os valores digitados em ordem são ", end='')
for c in list:
    print(c, end=' ')