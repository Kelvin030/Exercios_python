def sorteia(lista):
    from random import randint
    for num in range(1, 5):
        lista.append(randint(1, 10))

    print(f"Sorteando 5 valores da lista: ", end='')
    for n in lista:
        print(n, end=' ')
    print('PRONTO!!!')
def somapar(lista):
    soma = 0
    for value in lista:
        if value % 2 == 0:
            soma += value
    print(f"A soma dos valores PARES da lista: {lista} resulta em {soma}")


# Principal
numeros = []
sorteia(numeros)
somapar(numeros)
