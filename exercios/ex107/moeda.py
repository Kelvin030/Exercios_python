def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2


def aumentar(porcentagem,valor):
    aumen = (valor * porcentagem) / 100
    return valor + aumen


def diminuir(porcentagem,valor):
    dimin = (valor * porcentagem) / 100
    return valor - dimin


def moeda(valor):
    if valor in '.':
        valor = valor.replace(".", ",")
    return f'R${valor:.2f}'

n = input()
print(moeda(n))