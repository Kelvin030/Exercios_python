from datetime import date
data = date.today().year
cont = 0
cont2 = 0
for c in range(1, 8):
    n = int(input(f'em que ano a {c}° pessoa: '))
    if data - n >= 21:
        cont += 1
    elif data - n < 21:
        cont2 += 1
print(f'Ha {cont2} pessoas MENOR DE IDADE')
print(f'E a {cont} pessoas MAIOR DE IDADE')
