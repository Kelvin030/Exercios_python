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


def moeda(preço=0,moeda='R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')
