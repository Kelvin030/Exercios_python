from time import sleep
km = int(input('qual a velocidade atual do carro: '))
print('carregando...')
sleep(2)
if km <= 80:
    print('você esta dentro do limite de velocidade')
    print('Dirija com cuidado!')
else:
    n1 = (km - 80) * 7
    print(f'você não esta dentro do limite de velocidade\nvocê tera que pagar uma multa de R${n1 :.2f}')
