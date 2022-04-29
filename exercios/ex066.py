soma = contador = 0
while True:
    num = int(input('digite um valor (digite 999 para finalizar): '))
    if num == 999:
        break
    soma += num
    contador += 1
print(f'A soma de {contador} numeros é {soma}')
