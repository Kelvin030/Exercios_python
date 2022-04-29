termo = int(input('digite o TERMO: '))
razao = int(input('RAZÂO: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end=' ➔ ')
print('ACABOU')
