print('\033[36m=-=\033[m' * 15)
print('\033[34mAnalizador De Triangulos V2.0\033[m')
print('\033[36m=-=\033[m' * 15)


r1 = float(input('digite o primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print('é possivel formar o triangulo')
    if r1 == r2 == r3:
        print('tipo do triangulo: EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('tipo do triangulo: ESCALENO')
    else:
        print('Tipo de triangulo: ISÓSCELES')
else:
    print('não é possivel formar o triangulo')
