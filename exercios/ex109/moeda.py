def dobro(valor=0, monetario=False):
    resp = valor * 2
    if monetario:
        return moeda(resp)
    return resp


def metade(valor=0, monetario=False):
    resp = valor / 2
    if monetario:
        return moeda(resp)
    return resp


def aumentar(porcentagem=0,valor=0, monetario=False):
    aumen = (valor + (valor * porcentagem / 100))
    if monetario:
        return moeda(aumen)
    return aumen


def diminuir(porcentagem=0,valor=0, monetario=False):
    dimin = valor - (valor * porcentagem / 100)
    if monetario:
        return moeda(dimin)
    return dimin


def moeda(preço=0,moeda='R$'):
    resp = f'{moeda}{preço:.2f}'.replace('.', ',')
    return resp

