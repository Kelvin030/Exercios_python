menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input(f'digite o peço da {p}° pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o MAIOR peso é {maior}Kg')
print(f'o MENOR peso é {menor}KG')
