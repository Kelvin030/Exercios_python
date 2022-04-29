total = contador = numeros = 0
numeros = int(input('digite numerso para ser somados [digite 999 para parar]: '))
while numeros != 999:
    total += numeros
    contador += 1
    numeros = int(input('digite numerso para ser somados [digite 999 para parar]: '))
print(f'foram somados {contador} numeros e o total é {total}')
