maior = menor = contador = soma = 0
resposta = ''
while resposta == 's':
    numero = int(input('digite um numero:'))
    resposta = str(input('quer continuar[S/N]:')).lower().strip()
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print(f'A media dos {contador} numeros é {soma / contador :.1f}')
print(f'o maior numero digitado é {maior} e o menor é {menor}')
