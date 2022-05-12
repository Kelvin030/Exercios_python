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


def resumo(valor=0, aumento=10, redução=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analizado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor,True)}')
    print(f'Metade do preço: \t{metade(valor,True)}')
    print(f'{aumento}% de aumento: \t{aumentar(aumento,valor,True)}')
    print(f'{redução}% de redução:  \t{diminuir(redução,valor,True)}')
