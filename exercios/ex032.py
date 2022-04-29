ano = int(input('digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano {ano} é BISSXESTO')
else:
    print(f'o nao {ano} não é bissesto')
