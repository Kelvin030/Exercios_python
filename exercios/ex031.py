km = float(input('digite a distancia de viagem: '))
if km <= 200:
    print(f'o valor da passagem sera de R${0.50 * km :.2f}')
else:
    print(f'como a viagem é de {km} você pagara R${0.45 * km :.2f}')
